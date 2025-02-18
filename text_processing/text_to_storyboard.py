def create_storyboard(sentences):
    storyboard = []
    for sentence in sentences:
        scene = {"text": sentence, "actions": []}
        storyboard.append(scene)
    return storyboard