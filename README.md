# Data preprosessing
Data preprosessing for Master´s thesis on data quality

## Prerequisities
Python version 3.9.12 or higher

pandas 2.1.3

```pip install pandas```


## Preprosessing steps
### Pseudonymization
```
python Data_pseudonymization.py
```

### Counting data omissions
```
python Henkilosto.py

python Kayntitiedot.py

python Resurssit.py

python Toimenpide.py
```

##### Combining surgical appointment data omissions, personnel data omissions, resource data omissions and procedure data omissions by unique ID for distinctive surgical appointment, "TPKID".
```
python Yhdistaminen.py
```
### Sorting used accessories
```
python Tarvikkeet.py
```

## NOTE!

Code contains moc data for testing. Original data can not be included for privacy reasons.
