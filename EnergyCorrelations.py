# VzZ_bBj8-4sZ1m4VyZ6f
import quandl
import numpy
API_KEY  = "VzZ_bBj8-4sZ1m4VyZ6f"
quandl.ApiConfig.api_key = API_KEY

data = quandl.get("EIA/PET_RWTC_D", returns="numpy")
print(data)