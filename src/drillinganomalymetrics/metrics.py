import numpy as np
import pandas as pd

def logistic_function( Tarray,t ):
    return 1/(1+np.exp( -6+(12*(t-Tarray[0])/len(Tarray)) ))

def lambda_function(t, actualLabs,delta=360):
    if t in actualLabs:
        return 1
    elif (t<actualLabs[0]-delta):
        return 0
    else:
        return 1/(1+(actualLabs[0]-t)**2.0)

def calculate_accuracy_metrics( inputFilePaths,labelsPositive,formatDatesInputs,formatDateLabels,alpha=0.7, dateCol="Date",riskCol="SPR_Index",thersholdPredPos=0.67,delta=360 ):
    nT                      = 0
    sumRecall               = 0
    sumPrecisionDenominator = 0
    sumPrecisionNumerator   = 0
    allactlabs              = [  ]
    allpredlabs             = [  ]

    for i,T in enumerate( inputFilePaths ):
        consecutiveWindowsTotal = [  ]
        consecutiveWindowsPos   = [  ]

        #Getting the binary time series
        stickingOccurs      = False
        df                  = pd.read_csv( T,parse_dates=[dateCol],date_format=formatDatesInputs[i] )
        startLab, endLab    = labelsPositive[i]
        startLab            = pd.to_datetime( startLab,format=formatDateLabels )
        endLab              = pd.to_datetime( endLab,format=formatDateLabels )
        actualLabs          = np.where( (df[dateCol]>=startLab) & (df[dateCol]<=endLab),1,0 )
        if np.sum( actualLabs )>=1:
            stickingOccurs = True
            nT      = nT+1
        predLabs    = np.where( df[riskCol]>=thersholdPredPos,1,0 )
        allpredlabs.append(predLabs)
        allactlabs.append(actualLabs)

        #RECALL
        if stickingOccurs:
            timeStamps      = np.arange( np.argwhere(actualLabs==1)[0][0],np.argwhere(actualLabs==1)[-1][0]+1 )
            predAndTrue     = predLabs * actualLabs
            Si      = 1 if np.sum( predAndTrue )>=1 else 0
            Ut1     = np.sum( [predAndTrue[t]*logistic_function( timeStamps,t ) for t in timeStamps]  )
            Ut2     = np.sum( [logistic_function( timeStamps,t ) for t in timeStamps ] )
            SCi     = 0
            iStartActualEvent   = np.argwhere( actualLabs==1 )[0][0]
            iEndActualEvent     = np.argwhere( actualLabs==1 )[-1][0]
            flag        = False
            startCons   = -1000
            for j in range(iStartActualEvent,iEndActualEvent+1):
                if (predLabs[j]==1) and (not flag):
                    SCi += 1
                    startCons = j
                    flag = True
                elif (predLabs[j]==0):
                    if startCons>0: consecutiveWindowsPos.append( (startCons,j) )
                    flag = False
            Ci          = 1 if SCi==1 else 1/( np.sqrt(SCi) ) if SCi>1 else 0
            Ui          = Ci*Ut1/Ut2
            sumRecall   = sumRecall + ( alpha*Si  + (1-alpha)*Ui )


        # PRECISION
        SCi         = 0
        flag        = False
        startCons   = -1000
        for j in range(0,len(predLabs)):
            if (predLabs[j]==1) and (not flag):
                SCi         += 1
                startCons   = j
                flag        = True
            elif (predLabs[j]==0):
                if startCons>0: consecutiveWindowsTotal.append( (startCons,j) )
                flag        = False
        for k,window in enumerate(consecutiveWindowsTotal):
            sumPrecisionDenominator = sumPrecisionDenominator + 1
            if np.sum( predLabs[window[0]:window[1]+1]*actualLabs[window[0]:window[1]+1] ) !=0:
                timeStamps      = np.arange( np.argwhere(actualLabs==1)[0][0],np.argwhere(actualLabs==1)[-1][0]+1 )
                UAllInWindow    = np.sum( [lambda_function(t,timeStamps,delta) for t in np.arange(window[0],window[1]+1)] )/( window[1]-window[0]+1 )
            else:
                UAllInWindow        = 0
            sumPrecisionNumerator   = sumPrecisionNumerator + UAllInWindow
    
    recall      = (1/nT)*sumRecall
    precision   = sumPrecisionNumerator/sumPrecisionDenominator
    f1          = 2 / ((1/recall) + (1/precision))
    return recall,precision,f1,allpredlabs,allactlabs

