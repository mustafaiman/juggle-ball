import json
import os

class HighScores:
    def __init__(self):
        self.scores = []
        self.filename = "juggle_ball_high_scores.json"
        self.max_scores = 5
        self.load_scores()
    
    def load_scores(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.scores = json.load(f)
        except:
            self.scores = []
    
    def save_scores(self):
        with open(self.filename, 'w') as f:
            json.dump(self.scores, f)
    
    def add_score(self, name, score, max_balls):
        self.scores.append({
            'name': name,
            'score': score,
            'max_balls': max_balls
        })
        # Sort by score (primary) and max_balls (secondary)
        self.scores.sort(key=lambda x: (x['score'], x['max_balls']), reverse=True)
        # Keep only top 5
        self.scores = self.scores[:self.max_scores]
        self.save_scores()
    
    def is_high_score(self, score, max_balls):
        # Always a high score if we have less than max_scores
        if len(self.scores) < self.max_scores:
            return True
        # Check if this score would be in top 5
        temp_scores = self.scores.copy()
        temp_scores.append({
            'name': '',
            'score': score,
            'max_balls': max_balls
        })
        temp_scores.sort(key=lambda x: (x['score'], x['max_balls']), reverse=True)
        # If our score is in the first max_scores entries, it's a high score
        return any(s['score'] == score and s['max_balls'] == max_balls 
                  for s in temp_scores[:self.max_scores]) 