# NEDLab
## Create a virtual environment
```python3 -m venv venv```

## Activate Virtual Environment
```source venv/bin/activate```  

## Install packages
```pip install matplotlib mne pandas```

_Select interpreter_  
```Cmd+Shift+P```  
```Python: Select Interpreter```  
```Python 3.x.x 64-bit ('venv': venv)```  

# Database

## Preprocessing
| Initial Item              | Renamed/processed                                      | New  |
| ------------------------- | ------------------------------------------------------ | ---- |
| ParticipantID             | ParticipantID                                          | No   |
| EEG site                  | EEG site                                               | No   |
| Birthdate                 | Birthdate                                              | No   |
| EEG date                  | EEG date                                               | No   |
| Age at EEG (years)        | Age at EEG (years)                                     | No   |
| Sex at birth              | Sex at birth                                           | No   |
| Repeat Instrument         | Repeat Instrument                                      | No   |
| Genetic Status            | Genetic Status                                         | No   |
| Genetic Abnormality Type  | Genetic Abnormality Type                               | No   |
| Affected chromosome       | Affected chromosome                                    | No   |
| Full proximal boundary    | Full proximal boundary                                 | No   |
| Full distal boundary      | Full distal boundary                                   | No   |
| Human Genome Version      | Human Genome Version                                   | No   |
| family_member_type        | family_member_type                                     | Yes  |
| NVIQ_CIupr                | Estimated loss of Non-Verbal Intelligence Quotient     | Yes  |
| ORASD_upr                 | Estimated odds ratio for autism                        | Yes  |
| SRS_CIupr                 | Estimated gain of raw score of Social Responsiveness Scale | Yes  |
| PdN_CIupr                 | Estimated probability of being de novo                 | Yes  |
| sum_LOEUF_complete        | Sum LOEUF                                              | Yes  |



## Renamed columns
'NVIQ_CIupr': 'Estimated loss of Non-Verbal Intelligence Quotient'
    - 

'ORASD_upr': 'Estimated odds ratio for autism'
    - 

'SRS_CIupr': 'Estimated gain of raw score of Social Responsiveness Scale'
    - 

'PdN_CIupr': 'Estimated probability of being de novo'
    - 

'sum_LOEUF_complete': 'Sum LOEUF'
    - 
