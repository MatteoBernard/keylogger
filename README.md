# Keylogger

Simple keylogger listening to keyboard inputs

## Technologies

- Python
- VB Script

## Start keylogger 

```
git clone https://github.com/MatteoBernard/keylogger.git
pip install pynput
```

Change output file path as you want

```
cd .\keylogger\

# Launch with opened terminal
python .\keylogger.py

# Launch in background
.\run-keylogger.vbs
```

## Get stats

Get stats from keylogger output file, it will display the most used inputs
```
python .\input_stats.py
```

## Get patterns

Get patterns from keylogger output file, it will display the most used patterns
```
# Change min_length and min_count as you want
python .\patterns.py
```