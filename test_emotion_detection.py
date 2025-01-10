import unittest, requests
from EmotionDetector.emotion_detection import emotion_detector

def dominant_label(emotion_scores):
    # Returns the emotion with the highest score
    return max(emotion_scores, key=emotion_scores.get)

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        # Test case 1: Dominant emotion should be 'joy'
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(dominant_label(result_1), 'joy')

        # Test case 2: Dominant emotion should be 'anger'
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(dominant_label(result_2), 'anger')

        # Test case 3: Dominant emotion should be 'disgust'
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(dominant_label(result_3), 'disgust')

        # Test case 4: Dominant emotion should be 'sadness'
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(dominant_label(result_4), 'sadness')

        # Test case 5: Dominant emotion should be 'fear'
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(dominant_label(result_5), 'fear')

if __name__ == "__main__":
    unittest.main()
    