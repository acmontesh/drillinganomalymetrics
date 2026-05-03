# drillinganomalymetrics

[![Unit Tests](https://github.com/acmontesh/drillinganomalymetrics/actions/workflows/unit_tests.yaml/badge.svg)](https://github.com/acmontesh/drillinganomalymetrics/actions/workflows/unit_tests.yaml)  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://www.gnu.org/licenses/mit)
![Version](https://img.shields.io/badge/version-0.0.1-green)


------------------------

<strong>Description</strong><br>
drillinganomalymetrics is a Python package containing functions to compute accuracy metrics in the context of drilling anomaly detection. These metrics are design to reflect the proximity of a drilling anomaly prediction model to its ideal characteristics, namely:

<ul>
    <li>It effectively detects early signatures of all stuck pipe events without missing any,</li>
    <li>It effectively detects sticking symptoms as early as possible, allowing the drilling team to take actions to prevent risk escalation, and</li>
    <li>It does not generate false warnings, i.e., predictions of high risk in non-risky conditions.</li>
</ul>

<br>

<strong>Why New Metrics</strong><br>
In summary, traditional classification metrics fail to reflect how close a model is to the aforementioned ideal characteristics. More importantly, they often generate misleading values: bad models can get high scores and good models very low values. Moreoever, traditional metrics can become artificially inflated when used in a point-wise manner in drilling anomalies that develop over long periods of time. Examples are provided in Montes et al. (2025)—SPE-220725-PA. 


--------------------

<strong>Associated Theory/Methodology</strong><br>
The metrics provided in this package are thoroughly described and illustrated through examples in the context of stuck pipe prediction in Appendix B in the following open-access SPE Journal article: 
<ul>
    <li>Montes, A. C., Ashok, P., and van Oort, E. 2025. Review of Stuck Pipe Prediction Methods and Future Directions. <i>SPE Journal</i> <b>30</b>(06): 3334–3363. SPE-220725-PA. <a href="https://doi.org/10.2118/220725-pa">Link</a>.
    </li>
</ul>

------------



----------------------

### Abraham C. Montes
<a href="https://www.linkedin.com/in/abraham-c-montes-6661a841/">LinkedIn</a> | <a href="https://scholar.google.com/citations?user=Va0vQdsAAAAJ&hl=en">Google Scholar</a> | <a href="https://www.abraham-montes.com">Personal Website</a>

