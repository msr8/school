from json      import load as json_load
from pyperclip import copy as pyperclip_copy
import os

INP_FILENAME   = 'Ml - Practical.ipynb'
OUT_FILENAME   = 'Ml - Practical.md'
SCREENSHOS_DIR = os.path.join(os.getcwd(), 'screenshots')
PAGEBREAK      = r'<div style="page-break-after: always; visibility: hidden">\pagebreak</div>'
add_space      = lambda x: f'    {x}'


def deal_with_markdown(cell):
    md = ''.join(cell['source'])
    if md == '<br><br><br>': return f'\n\n{PAGEBREAK}\n\n'
    else                   : return f'{md[2:]}\n\n<br>\n\n' # Doing md[2:] to convert `### QUES` to `# QUES`

def deal_with_code(cell):
    code    = ''.join(cell['source'])
    code    = code.replace(', index=True','').replace('display_df()','display_df').replace('display_df','print')
    outputs = cell['outputs']

    ret = f'## CODE\n\n```python\n{code}\n```\n\n<br>\n\n## OUTPUT\n\n'

    for output in outputs:
        # If it is a text output
        if output['output_type'] == 'stream':
            texts = map(add_space, output['text'])
            # Remove tensorflow warnings
            texts = [ i for i in texts if not 'tensorflow' in i.lower() ]
            out = ''.join(texts)
            ret += f'{out}\n'
        
        elif output['output_type'] == 'display_data':
            # If it is markdown, ie just tables
            if output['data'].get('text/markdown'):
                mds  = output['data']['text/markdown']
                ret += ''.join(mds) + '\n'
            # Else if its a png (seaborn plot)
            elif output['data'].get('image/png'):
                img  = output['data']['image/png']
                ret += f'<center>\n\n<img src="data:image/png;base64,{img}">\n\n</center>\n\n'
            else:
                raise ValueError(f'Unknown output type: {output["output_type"]}')
    
    return ret





ret = f'{PAGEBREAK}\n\n'
# ret = ''

with open(INP_FILENAME) as f:
    ipynb = json_load(f)

cells = ipynb['cells']
cells = cells[2:-1]

for cell in cells:
    if cell['cell_type'] == 'markdown':
        ret += deal_with_markdown(cell)
    elif cell['cell_type'] == 'code':
        ret += deal_with_code(cell)
    else:
        raise ValueError(f'Unknown cell type: {cell["cell_type"]}')





with open(OUT_FILENAME, 'w') as f:
    f.write(ret)
pyperclip_copy(ret)
    



