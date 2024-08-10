# JSONLgenerator
an easy way to create JSONL files for fine-tuning openai models. [Web app here](https://jsonlgenerator.streamlit.app/)
Just type in your prompts, completions and specify prompt/completion seperators and this app will create a JSON file for you.  
## from the command line
simply run `python create_jsonl.py -h` for instructions on how to get started and avaliable command line options.  
Once you are ready to create your JSONL file, redirect the output to the file you want  
```
python create_jsonl.py [options] > output.jsonl
```
You can ignore the other files in this repo, they are either impelementation details or used for the webapp.  
## Contribution
Any and all contributions big and small are very appreciated.  This project is ideal for a python programmer looking to make a first pull-request (lot's of low-hanging fruit!)
