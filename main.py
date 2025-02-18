from text_processing.nlp_model import process_text
from text_processing.text_to_storyboard import create_storyboard
from storyboarding.create_storyboard import visualize_storyboard
from video_generation.generate_frames import generate_frames
from video_generation.create_video import create_video

def main():
    text = (
        "Tenali Raman and the Talking Pot\n"
        "Once upon a time in the grand kingdom of Vijayanagara, ruled by the wise King Krishnadevaraya, "
        "there lived a clever and witty man named Tenali Raman. Everyone in the kingdom admired Tenali for his sharp mind and quick wit. "
        "But one day, something very strange happened—something so unusual that even Tenali himself was left scratching his head!\n\n"
        "The King’s Strange Dream\n"
        "One fine morning, King Krishnadevaraya called Tenali Raman to the royal court.\n\n"
        "\"Tenali!\" the king said with a serious face. \"I had a strange dream last night. In my dream, a pot started talking to me!\"\n\n"
        "\"A talking pot?\" Tenali Raman asked, raising an eyebrow.\n\n"
        "\"Yes!\" the king continued. \"The pot said, 'Oh King, I am the most valuable treasure in your entire kingdom! "
        "Find me, and you will become the richest king in the world!’\"\n\n"
        "The entire court gasped. Ministers whispered among themselves.\n\n"
        "\"Tenali, I order you to find this talking pot! It must be hidden somewhere in our kingdom,\" the king said.\n\n"
        "Tenali Raman, who was always up for a good challenge, bowed and said, \"Your Majesty, give me three days, and I will find your talking pot!\"\n\n"
        "The Great Pot Hunt\n"
        "Tenali started his search by going to every pottery shop in the kingdom.\n\n"
        "\"Do you have a talking pot?\" he asked the potters.\n\n"
        "The potters looked at him like he had lost his mind.\n\n"
        "\"A talking pot? Sir, our pots only talk when they fall and break!\" one potter joked.\n\n"
        "\"Hmm… maybe I need to find a special pot,\" Tenali thought.\n\n"
        "For three days, he searched high and low, but there was no talking pot to be found. Just when he was about to give up, "
        "he saw an old beggar sitting by the temple, laughing to himself.\n\n"
        "\"Why are you laughing, old man?\" Tenali asked.\n\n"
        "\"Because, sir, people chase foolish dreams instead of using their brains!\" the beggar replied.\n\n"
        "Tenali’s eyes lit up. \"That’s it!\" he thought.\n\n"
        "The Talking Pot is Found!\n"
        "The next day, Tenali walked into the king’s court carrying a large pot.\n\n"
        "\"Your Majesty, I have found the talking pot!\" he declared.\n\n"
        "The king was shocked. \"Really? Let me hear it speak!\"\n\n"
        "Tenali placed the pot on the floor and knocked on it three times. Then, in a deep voice, he said, \"Oh mighty King! "
        "The real treasure is not inside me but inside Tenali Raman’s brain!\"\n\n"
        "The king’s eyes widened. \"Wait… did the pot just talk?!\"\n\n"
        "\"Yes, Your Majesty!\" Tenali nodded. \"But listen carefully to what it says!\" He knocked on the pot again and, in a funny voice, said, "
        "\"Oh great King, don't waste time chasing silly dreams! Use your wisdom instead!\"\n\n"
        "The entire court burst into laughter! The ministers clapped, and even the king chuckled.\n\n"
        "\"Tenali! You tricked me!\" the king said, laughing. \"But you also taught me a valuable lesson. Instead of chasing imaginary treasures, I should use my wisdom!\"\n\n"
        "The king rewarded Tenali with a bag of gold, and from that day on, he never believed in talking pots again!\n\n"
        "And so, once again, Tenali Raman used his brilliant mind to turn a royal problem into a royal joke!\n\n"
        "Moral of the Story:\n"
        "🔹 Don’t waste time chasing impossible things—use your intelligence to find real solutions!\n"
        "🔹 And most importantly… never believe a talking pot! 😆"
    )

    sentences = process_text(text)
    storyboard = create_storyboard(sentences)
    visualize_storyboard(storyboard)
    frames = generate_frames(storyboard)
    create_video(frames, text)

if __name__ == "__main__":
    main()