# CalcTopsis

* CalcTopsis is a Python package implementing Topsis method sed for multi-criteria decision analysis.
* Topsis stands for **T**echnique for **O**rder of **P**reference by **S**imilarity to **I**deal **S**olution

* Just provide your input attributes and it will give you the results


## Installation

`$ pip install calctopsis`

In the commandline, you can write as -
`$ python <script_name> <path to input_data_file_name> <weights as strings> <impacts as strings> <result_file_name>`

E.g for input data file as data.csv, command will be like
`$ python topsis.py data.csv "1,1,1,1" "+,+,-,+" output.csv`

This will print all the output attribute values along with the Rank column, in a tabular format

## License
MIT