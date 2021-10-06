## Data from a pi using exoedge
### Background on Creating Python Libraries
see: https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

### Setup
1. Clone this repo to your raspberry pi
2. `pip3 install wheel`
3. `pip3 install setuptools`
4. `pip3 install twine`
5. Change the functions within `myfunctions.py` as you see fit
6. Build the library `python3 setup.py bdist_wheel` from the root folder of this repo
7. Install to your computer `pip3 install /path/to/.whl --force-reinstall`
8. Use in config_io something like this: 
```
{
  "function": "minutes_from_now",
  "module": "exoedgesource",
  "parameters": {
    "minutes": 30
  },
  "positionals": []
}
```