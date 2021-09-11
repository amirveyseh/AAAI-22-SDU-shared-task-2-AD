import argparse
import json

def predict(data, diction):
    predictions = []
    for d in data:
        pred = {
            'ID': d['ID'],
            'label': ''
        }
        sent = d['sentence']
        candids = diction[d['acronym']]
        highest_score = 0
        best = ''
        for candid in candids:
            score = 0
            cand_words = candid.split()
            for w in cand_words:
                if w in sent:
                    score += 1
            score /= len(cand_words)
            if score > highest_score:
                highest_score = score
                best = candid
        if best == '':
            best = candids[0]
        pred['label'] = best
        predictions.append(pred)
    return predictions

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', type=str,
                        help='Path to the input file (e.g., dev.json)')
    parser.add_argument('-diction', type=str,
                        help='Path to the dictionary')
    parser.add_argument('-output', type=str,
                        help='Prediction file path')
    args = parser.parse_args()

    ## READ data
    with open(args.input) as file:
        data = json.load(file)
    with open(args.diction) as file:
        diction = json.load(file)

    ## Predict
    predictions = predict(data, diction)

    ## Save
    with open(args.output, 'w') as file:
        json.dump(predictions, file)