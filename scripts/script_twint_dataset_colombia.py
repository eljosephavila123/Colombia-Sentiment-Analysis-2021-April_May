import twint

config = twint.Config()
config.Store_csv = True
config.Search = "colombia AND reforma"
config.Since = "2020-04-01"
config.Lang = "es"
config.Output = "reforma_colombia.csv"
twint.run.Search(config)
