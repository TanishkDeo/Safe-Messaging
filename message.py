from googleapiclient import discovery

API_KEY = 'XXXX'
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)


def toxicfinder(comment):
    analyze_request = {
        'comment': {'text': "{0}".format(comment)},
        'requestedAttributes': {'TOXICITY': {}}
    }
    response = service.comments().analyze(body=analyze_request).execute()

    import json
    data = json.dumps(response)
    a = data[91:]
    b = a.split(",", 1)
    c = float(b[0])
    score = round((c*100), 2)
    print(score)
    return score
