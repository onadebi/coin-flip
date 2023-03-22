import logging;
import json;
import math;
import random;

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Heads and Tails count.')

    count: int = math.ceil(float(req.params.get('count'))) if (req.params.get('count') is not None) else 9;
        
    if count:
        heads: int = 0;
        tails: int = 0;
        for i in range(int(count)):
            numb = random.randint(0,1)
            if(numb == 1):
                print("Heads!")
                heads = heads+1
            else:
                print("Tails!")
                tails = tails+1
        message: str=  f'Head wins by {heads-tails} point(s).' if (heads > tails) else f'Tail wins by {tails-heads} point(s).';
        return func.HttpResponse(json.dumps({'count': count, 'heads': heads, 'tails':tails,'message':message }), status_code=200)
    else:
        return func.HttpResponse(
             "Invalid parameters passed.",
             status_code=400
        )
