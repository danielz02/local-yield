# Requirement

`Python 3`

`tqdm`

`wget`

# Usage

+ Run `sh yank_data.sh` with desired parameters to query a public API with every zip code in the United States and store the raw Json responses
+ Run `parse_csv.py` to parse Json files into CSV
+ Some response could come up empty due to network issues. Any zip code with Json response that the script can't parse will be written into `error.log`
+ Run `request_empty.sh` to send requests again for failed zip codes

# Credit

Thanks [this GitHub Gist](https://gist.github.com/abatko/ee7b24db82a6f50cfce02afafa1dfd1e) for the mapping between zip code and its coordinates.