import random
import time
import os

def clear_screen():
    """Clear the terminal screen for better user experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Dictionary containing all our mood-based recommendations
mood_recommendations = {
    "happy": {
        "playlists": [
            "Happy Hits! - Upbeat pop songs to brighten your day",
            "Good Vibes - Positive and uplifting tunes",
            "Feel-Good Indie - Indie tracks with positive vibes",
            "Happiness Boost - Classic happy songs from all decades",
            "Sunny Day - Perfect for a sunny day outside",
            "Mood Booster - Instant happiness guaranteed",
            "Happy Dance - Get moving with these happy beats",
            "Cheerful Classics - Timeless happy songs",
            "Upbeat Anthems - Popular songs to lift your spirits",
            "Smile Songs - Music that'll make you grin"
        ],
        "activities": [
            "Call a friend who makes you laugh",
            "Go for a walk in the sunshine",
            "Try a new recipe you've been wanting to make",
            "Dance around to your favorite song",
            "Write down 3 things you're grateful for",
            "Plant something or tend to your plants",
            "Take photos of things that make you happy",
            "Treat yourself to your favorite dessert",
            "Do a random act of kindness for someone",
            "Watch funny videos on YouTube"
        ],
        "quotes": [
            ""Happiness is not something ready-made. It comes from your own actions." – Dalai Lama",
            ""The most wasted of all days is one without laughter." – E. E. Cummings",
            ""Happiness is when what you think, what you say, and what you do are in harmony." – Mahatma Gandhi",
            ""The purpose of our lives is to be happy." – Dalai Lama",
            ""Count your age by friends, not years. Count your life by smiles, not tears." – John Lennon",
            ""Happiness is a warm puppy." – Charles M. Schulz",
            ""The happiest people don't have the best of everything, they make the best of everything." – Anonymous",
            ""Happiness is not a goal; it is a by-product." – Eleanor Roosevelt",
            ""The secret of happiness is freedom, the secret of freedom is courage." – Thucydides",
            ""Be happy with what you have. Be excited about what you want." – Alan Cohen"
        ]
    },
    "sad": {
        "playlists": [
            "Sad Songs for Crying - When you need to let it all out",
            "Melancholy Mood - Gentle and thoughtful sad songs",
            "Rainy Day Feels - Perfect for staring out the window",
            "Heartbreak Hotel - Songs for when love hurts",
            "Sad Piano Pieces - Instrumental tracks for reflection",
            "Emotional Ballads - Powerful sad songs from great vocalists",
            "Sad But Beautiful - Finding beauty in sadness",
            "Acoustic Heartache - Stripped-down sad songs",
            "Down Tempo - Slow beats for contemplation",
            "Sad Classics - Timeless melancholy music"
        ],
        "activities": [
            "Write in a journal about how you're feeling",
            "Take a long, warm shower or bath",
            "Watch a sad movie (sometimes it helps to cry it out)",
            "Go for a quiet walk in nature",
            "Wrap up in a cozy blanket with a warm drink",
            "Listen to rain sounds or calming nature sounds",
            "Look through old photos that bring back good memories",
            "Call a supportive friend or family member",
            "Practice gentle yoga or stretching",
            "Create some art expressing how you feel"
        ],
        "quotes": [
            ""Even the darkest night will end and the sun will rise." – Victor Hugo",
            ""There are moments when I wish I could roll back the clock and take all the sadness away, but I have a feeling that if I did, the joy would be gone as well." – Nicholas Sparks",
            ""Sadness is but a wall between two gardens." – Kahlil Gibran",
            ""The way sadness works is one of the strange riddles of the world. If you are stricken with a great sadness, you may feel as if you have been set aflame, not only because of the enormous pain but also because your sadness may spread over your life." – Lemony Snicket",
            ""Tears are words that need to be written." – Paulo Coelho",
            ""Behind every sweet smile, there is a bitter sadness that no one can ever see and feel." – Anonymous",
            ""Sadness flies away on the wings of time." – Jean de La Fontaine",
            ""The good life is not one immune to sadness but one in which suffering contributes to our development." – Alain de Botton",
            ""When you're feeling down, remember it's only a mood, not the truth about your life." – Anonymous",
            ""Sometimes you've got to be able to listen to yourself and be okay with no one else understanding." – Anonymous"
        ]
    },
    "energetic": {
        "playlists": [
            "Energy Boost - High tempo tracks to get moving",
            "Power Workout - Ultimate exercise motivation",
            "Morning Energy - Start your day with a bang",
            "Dance Party - Non-stop energy for dancing",
            "Adrenaline Rush - Tracks that get your heart pumping",
            "Power Hour - One hour of pure energy",
            "Motivation Mix - Songs to fuel your productivity",
            "Energy Anthems - Classic high-energy tracks",
            "Upbeat Indie - Energy from the alternative scene",
            "Electric Energy - Electronic beats to boost your mood"
        ],
        "activities": [
            "Go for a run or brisk walk",
            "Have an impromptu dance party",
            "Tackle that home project you've been putting off",
            "Rearrange your furniture for a fresh perspective",
            "Try a new HIIT workout routine",
            "Go biking or skating outdoors",
            "Clean while dancing to upbeat music",
            "Start a creative project that requires focus",
            "Challenge yourself to learn a dance routine",
            "Call an energetic friend for a spontaneous hangout"
        ],
        "quotes": [
            ""Energy and persistence conquer all things." – Benjamin Franklin",
            ""The energy of the mind is the essence of life." – Aristotle",
            ""Action is the foundational key to all success." – Pablo Picasso",
            ""Life is like riding a bicycle. To keep your balance, you must keep moving." – Albert Einstein",
            ""Your body is a reflection of your lifestyle." – Anonymous",
            ""The higher your energy level, the more efficient your body. The more efficient your body, the better you feel." – Tony Robbins",
            ""Positive energy knows no boundaries." – Anonymous",
            ""Energy is contagious, positive and negative alike." – Anonymous",
            ""If you want to fly, you have to give up the things that weigh you down." – Anonymous",
            ""Push yourself because no one else is going to do it for you." – Anonymous"
        ]
    },
    "needs uplifting": {
        "playlists": [
            "Uplifting Anthems - Songs to raise your spirits",
            "Motivation Mix - Music for an instant mood boost",
            "Positive Vibes - Feel-good tracks for tough days",
            "Inspiring Instrumentals - Uplifting without words",
            "Cheer Up Songs - Can't help but smile",
            "Encouragement Playlist - You've got this!",
            "Hope & Inspiration - Songs about overcoming",
            "Mood Lifter - Get out of that funk",
            "Positive Pop - Upbeat pop songs to boost morale",
            "Chill Positive Vibes - Gentle uplifting tunes"
        ],
        "activities": [
            "Watch videos of people being kind to each other",
            "Make a list of your personal wins, no matter how small",
            "Send a message to someone you care about",
            "Take a short walk somewhere green",
            "Do something creative without judging the result",
            "Looking at photos of cute animals",
            "Listen to an uplifting podcast or TED talk",
            "Make yourself a special, nourishing meal",
            "Do 10 minutes of stretching while listening to nature sounds",
            "Write down 5 things you're looking forward to"
        ],
        "quotes": [
            ""This too shall pass." – Persian Proverb",
            ""You are never too old to set another goal or to dream a new dream." – C.S. Lewis",
            ""It's not whether you get knocked down, it's whether you get up." – Vince Lombardi",
            ""Believe you can and you're halfway there." – Theodore Roosevelt",
            ""Keep your face always toward the sunshine, and shadows will fall behind you." – Walt Whitman",
            ""The only way to do great work is to love what you do." – Steve Jobs",
            ""Just keep swimming." – Dory, Finding Nemo",
            ""When you come to the end of your rope, tie a knot and hang on." – Franklin D. Roosevelt",
            ""Every moment is a fresh beginning." – T.S. Eliot",
            ""Your current situation is not your final destination." – Anonymous"
        ]
    },
    "post break-up": {
        "playlists": [
            "Break-Up Anthems - Empowering songs after heartbreak",
            "Look What You Made Me Do - Taylor Swift & other revenge tracks",
            "Moving On & Getting Over - Songs about healing",
            "I'm Better Without You - Empowerment after heartbreak",
            "Confidence Boost - Remind yourself how amazing you are",
            "Fresh Start - New beginnings after a relationship",
            "Independent & Thriving - Songs celebrating independence",
            "Glow Up Playlist - Time to focus on yourself",
            "Breakup to Breakthrough - Transforming pain to power",
            "So Over You - When you're ready to laugh about it"
        ],
        "activities": [
            "Marie Kondo your space - remove things that don't bring joy",
            "Try a bold new hairstyle or outfit",
            "Plan a solo trip or adventure",
            "Start a new fitness routine or challenge",
            "Host a 'newly single' party with friends",
            "Create a vision board for your new future",
            "Take yourself on a date to somewhere you've wanted to go",
            "Delete old photos (or at least move them to a hidden folder)",
            "Learn a new skill you've always been interested in",
            "Write a letter expressing your feelings (that you don't send)"
        ],
        "quotes": [
            ""Sometimes good things fall apart so better things can fall together." – Marilyn Monroe",
            ""The best revenge is massive success." – Frank Sinatra",
            ""Don't cry because it's over, smile because it happened." – Dr. Seuss",
            ""You can love them, forgive them, want good things for them...but still move on without them." – Mandy Hale",
            ""The hardest part isn't letting you go, but rather learning to start over." – Anonymous",
            ""Hearts will never be practical until they are made unbreakable." – The Wizard of Oz",
            ""It's not the end of the world to be rejected or to have somebody not love you. It just means you weren't meant to be." – Taylor Swift",
            ""The emotion that can break your heart is sometimes the very one that heals it." – Nicholas Sparks",
            ""The hottest love has the coldest end." – Socrates",
            ""I'm proud of my heart. It's been played, burned, and broken, but somehow still works." – Anonymous"
        ]
    },
    "angry": {
        "playlists": [
            "Rage Room - Heavy rock and metal for anger release",
            "Anger Management - Express and process your frustration",
            "Primal Scream - Let it all out with these intense tracks",
            "Righteous Anger - Songs about justified outrage",
            "Cathartic Rock - Process emotions through powerful rock",
            "Fight The Power - Songs about standing up",
            "Fury Beats - Fast-paced tracks for anger release",
            "Vent Session - Music to help you express your anger",
            "Defiance Playlist - For when you won't back down",
            "Controlled Chaos - Intense but structured music"
        ],
        "activities": [
            "Go for a hard, fast run",
            "Punch a pillow or scream into it",
            "Write an angry letter (that you don't send)",
            "Clean vigorously - scrub something that needs it",
            "Do an intense workout session",
            "Break something safely (like tear paper or pop bubble wrap)",
            "Draw or paint with bold, angry strokes",
            "Go to a batting cage or driving range",
            "Throw ice cubes at a shower wall or bathtub",
            "Do breathing exercises: in for 4, hold for 4, out for 6"
        ],
        "quotes": [
            ""For every minute you remain angry, you give up sixty seconds of peace of mind." – Ralph Waldo Emerson",
            ""Speak when you are angry, and you will make the best speech you'll ever regret." – Ambrose Bierce",
            ""Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured." – Mark Twain",
            ""Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned." – Buddha",
            ""When angry, count to ten before you speak. If very angry, count to one hundred." – Thomas Jefferson",
            ""Anger is never without a reason, but seldom with a good one." – Benjamin Franklin",
            ""You will not be punished for your anger, you will be punished by your anger." – Buddha",
            ""Whatever is begun in anger, ends in shame." – Benjamin Franklin",
            ""Anger is a valid emotion. It's only bad when it takes control and makes you do things you don't want to do." – Anonymous",
            ""Anybody can become angry — that is easy, but to be angry with the right person and to the right degree and at the right time and for the right purpose, and in the right way — that is not within everybody's power and is not easy." – Aristotle"
        ]
    },
    "tired": {
        "playlists": [
            "Gentle Relaxation - Soft music for tired minds",
            "Drift Away - Perfect for falling asleep",
            "Calming Classics - Peaceful classical music",
            "Sleepy Time - Songs to help you unwind",
            "Acoustic Lullabies - Gentle guitar for relaxation",
            "Ambient Space - Peaceful atmospheric sounds",
            "Piano Dreams - Soft piano for tired moments",
            "Nature Sleep Sounds - Rain, waves and forest sounds",
            "Chill Lo-Fi - Low-key beats for relaxation",
            "Meditation Music - Help your mind and body rest"
        ],
        "activities": [
            "Take a warm bath with essential oils",
            "Make yourself a cup of chamomile tea",
            "Do 10 minutes of gentle stretching",
            "Wrap yourself in a soft blanket and just rest",
            "Try a guided relaxation meditation",
            "Apply a cool face mask and lie down",
            "Listen to a calming podcast or audiobook",
            "Give yourself a gentle hand or foot massage",
            "Dim the lights and set a relaxing atmosphere",
            "Write down tasks for tomorrow so you can let go of them tonight"
        ],
        "quotes": [
            ""Rest when you're weary. Refresh and renew yourself, your body, your mind, your spirit." – Ralph Marston",
            ""Sometimes the most productive thing you can do is rest." – Anonymous",
            ""Your body is telling you something. Listen to it." – Anonymous",
            ""Sleep is the best meditation." – Dalai Lama",
            ""Even the strongest minds need rest." – Anonymous",
            ""There is virtue in work and there is virtue in rest. Use both and overlook neither." – Alan Cohen",
            ""If you get tired, learn to rest, not to quit." – Banksy",
            ""Almost everything will work again if you unplug it for a few minutes, including you." – Anne Lamott",
            ""Rest is not idleness, and to lie sometimes on the grass under trees on a summer's day, listening to the murmur of the water, or watching the clouds float across the sky, is by no means a waste of time." – John Lubbock",
            ""A good rest is half the work." – Yugoslav Proverb"
        ]
    },
    "love songs": {
        "playlists": [
            "Love Ballads - Classic romantic songs",
            "Modern Love - Contemporary love songs",
            "Romantic Mood - Create the perfect atmosphere",
            "Forever Love - Songs about everlasting love",
            "Love Language - Express your feelings through music",
            "Acoustic Love Songs - Intimate and heartfelt",
            "R&B Love - Smooth and soulful romance",
            "First Dance - Perfect wedding songs",
            "Love Poems - Poetic lyrics about love",
            "Date Night - Set the mood for a special evening"
        ],
        "activities": [
            "Write a heartfelt letter to someone you love",
            "Plan a surprise date night",
            "Make a photo album of special memories",
            "Cook a romantic meal",
            "Slow dance in your living room",
            "Learn to say 'I love you' in different languages",
            "Create a playlist of songs that remind you of your loved one",
            "Take a romantic walk under the stars",
            "Plant something together that will grow over time",
            "Take a relationship quiz together to learn more about each other"
        ],
        "quotes": [
            ""I love you not because of who you are, but because of who I am when I am with you." – Roy Croft",
            ""To love and be loved is to feel the sun from both sides." – David Viscott",
            ""Love is composed of a single soul inhabiting two bodies." – Aristotle",
            ""When I saw you I fell in love, and you smiled because you knew." – William Shakespeare",
            ""The best thing to hold onto in life is each other." – Audrey Hepburn",
            ""Love is when the other person's happiness is more important than your own." – H. Jackson Brown Jr.",
            ""You know you're in love when you can't fall asleep because reality is finally better than your dreams." – Dr. Seuss",
            ""Being deeply loved by someone gives you strength, while loving someone deeply gives you courage." – Lao Tzu",
            ""I would rather spend one lifetime with you, than face all the ages of this world alone." – J.R.R. Tolkien",
            ""Love isn't something you find. Love is something that finds you." – Loretta Young"
        ]
    },
    "stressed": {
        "playlists": [
            "Stress Relief - Calming songs for anxious moments",
            "Peaceful Piano - Gentle instrumentals to reduce stress",
            "Calm Mind - Music to help you breathe",
            "Meditation Focus - Ambient sounds for stress reduction",
            "Ocean Waves - Natural sounds for relaxation",
            "Anxiety Relief - Songs to calm your nerves",
            "Deep Breath - Tracks timed for breathing exercises",
            "Gentle Jazz - Smooth jazz for unwinding",
            "Forest Sounds - Nature's stress reliever",
            "Calming Classical - Timeless pieces for relaxation"
        ],
        "activities": [
            "Try the 5-5-5 breathing technique (inhale for 5, hold for 5, exhale for 5)",
            "Go for a mindful walk, focusing on your surroundings",
            "Make a cup of tea and drink it slowly, focusing on the sensation",
            "Squeeze a stress ball or play with putty/slime",
            "Draw or color in a coloring book",
            "Do a body scan meditation",
            "Tense and release each muscle group in your body",
            "Write down what's stressing you, then write possible solutions",
            "Take a short nap if possible",
            "Try progressive muscle relaxation"
        ],
        "quotes": [
            ""The greatest weapon against stress is our ability to choose one thought over another." – William James",
            ""Stress is caused by being 'here' but wanting to be 'there'." – Eckhart Tolle",
            ""In times of stress, the best thing we can do is to lie down and listen to the earth, admire the calm of the sea, enjoy the tender beauty of a flower." – Anonymous",
            ""It's not the load that breaks you down, it's the way you carry it." – Lou Holtz",
            ""The time to relax is when you don't have time for it." – Sydney J. Harris",
            ""Life isn't as serious as the mind makes it out to be." – Eckhart Tolle",
            ""Tension is who you think you should be. Relaxation is who you are." – Chinese Proverb",
            ""You don't have to control your thoughts. You just have to stop letting them control you." – Dan Millman",
            ""Rule number one is, don't sweat the small stuff. Rule number two is, it's all small stuff." – Robert Eliot",
            ""Breathe. Let go. And remind yourself that this very moment is the only one you know you have for sure." – Oprah Winfrey"
        ]
    },
    "bored": {
        "playlists": [
            "Discovery Mix - Find new music you'll love",
            "Genre Explorers - Dive into new musical territories",
            "Unusual Covers - Familiar songs, unexpected versions",
            "Bizarre & Interesting - Weird but wonderful tracks",
            "Musical Adventure - Songs that tell a story",
            "Global Sounds - Music from around the world",
            "Decade Dive - Explore a new musical era",
            "Hidden Gems - Great songs you've probably never heard",
            "Musical Mashups - Unexpected combinations",
            "Conversation Starters - Music that gets people talking"
        ],
        "activities": [
            "Learn to juggle using YouTube tutorials",
            "Start a 30-day challenge (drawing, fitness, etc.)",
            "Look up a new recipe and cook something exotic",
            "Rearrange your furniture for a fresh perspective",
            "Start a blog about something you're passionate about",
            "Learn how to say basic phrases in a new language",
            "Do a virtual tour of a famous museum",
            "Make a bucket list of things you want to do",
            "Clean out and organize a junk drawer",
            "Look up DIY science experiments you can do at home"
        ],
        "quotes": [
            ""Boredom is the dream bird that hatches the egg of experience." – Walter Benjamin",
            ""The cure for boredom is curiosity. There is no cure for curiosity." – Dorothy Parker",
            ""When you pay attention to boredom, it gets unbelievably interesting." – Jon Kabat-Zinn",
            ""Boredom always precedes a period of great creativity." – Robert M. Pirsig",
            ""Your life is as good as your mindset. If you're bored, you're not paying attention." – Anonymous",
            ""The life of the creative person is led, directed and controlled by boredom. Avoiding boredom is one of our most important purposes." – Saul Steinberg",
            ""When you're bored with yourself, marry and be bored with someone else." – David Pryce-Jones",
            ""The two enemies of human happiness are pain and boredom." – Arthur Schopenhauer",
            ""Boredom is simply the absence of an interesting perspective." – Anonymous",
            ""Is life not a thousand times too short for us to bore ourselves?" – Friedrich Nietzsche"
        ]
    },
    "exercise": {
        "playlists": [
            "Workout Beats - High-energy tracks with perfect BPM",
            "Running Motivation - Perfect pace-setting songs",
            "Gym Heroes - Ultimate workout anthems",
            "HIIT Mix - Interval training with matching tempos",
            "Cardio Blast - Keep your heart rate up",
            "Strength Training - Heavy beats for lifting",
            "Power Hour - Full 60-minute workout soundtrack",
            "Yoga Flow - Rhythmic tracks for moving meditation",
            "Sports Anthems - Classic motivation tracks",
            "Cool Down - Post-workout relaxation"
        ],
        "activities": [
            "Try a 7-minute workout app",
            "Follow a YouTube HIIT workout",
            "Create your own circuit training with 5 exercises",
            "Go for a run with interval sprints",
            "Do a plank challenge (how long can you hold it?)",
            "Try a new fitness class (online or in-person)",
            "Do jumping jacks during TV commercial breaks",
            "Learn a short dance routine from TikTok or YouTube",
            "Go for a bike ride with varying intensity",
            "Create an obstacle course in your home or backyard"
        ],
        "quotes": [
            ""No pain, no gain. Shut up and train." – Anonymous",
            ""The only bad workout is the one that didn't happen." – Anonymous",
            ""Your body can stand almost anything. It's your mind that you have to convince." – Anonymous",
            ""Fitness is not about being better than someone else. It's about being better than you used to be." – Anonymous",
            ""The difference between try and triumph is just a little umph!" – Marvin Phillips",
            ""The only place where success comes before work is in the dictionary." – Vidal Sassoon",
            ""Sweat is just fat crying." – Anonymous",
            ""Exercise is king. Nutrition is queen. Put them together and you've got a kingdom." – Jack LaLanne",
            ""You don't have to be extreme, just consistent." – Anonymous",
            ""What seems impossible today will one day become your warm-up." – Anonymous"
        ]
    },
    "sporty": {
        "playlists": [
            "Sports Anthems - Classic stadium songs",
            "World Cup Hits - Football/soccer celebration songs",
            "Champion Sound - Tracks from sporting events",
            "Olympic Spirit - Songs that celebrate athletic achievement",
            "Training Montage - Songs from sports movies",
            "Game Day - Get pumped for the big match",
            "Victory Lap - Celebrate your win",
            "Team Spirit - Songs about unity and teamwork",
            "Waka Waka & Beyond - Global sports celebration songs",
            "Sports Movie Soundtrack - Inspiring themes from sports films"
        ],
        "activities": [
            "Watch highlights from a classic sports match",
            "Practice a sports skill for 20 minutes",
            "Set up a mini-golf course in your home",
            "Challenge someone to a push-up contest",
            "Learn a new trick with a ball (juggling, spinning, etc.)",
            "Watch a sports movie for motivation",
            "Create a sports-themed trivia quiz for friends",
            "Try a sports-inspired workout routine",
            "Do a tournament bracket for something fun at home",
            "Plan a sports day with friends"
        ],
        "quotes": [
            ""Champions keep playing until they get it right." – Billie Jean King",
            ""You miss 100% of the shots you don't take." – Wayne Gretzky",
            ""It's not whether you get knocked down, it's whether you get up." – Vince Lombardi",
            ""The more difficult the victory, the greater the happiness in winning." – Pelé",
            ""It ain't over till it's over." – Yogi Berra",
            ""Champions aren't made in gyms. Champions are made from something they have deep inside them." – Muhammad Ali",
            ""You can't put a limit on anything. The more you dream, the farther you get." – Michael Phelps",
            ""I've missed more than 9,000 shots in my career. I've lost almost 300 games. Twenty-six times I've been trusted to take the game-winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed." – Michael Jordan",
            ""It's hard to beat a person who never gives up." – Babe Ruth",
            ""The only way to prove that you're a good sport is to lose." – Ernie Banks"
        ]
    }
}

def display_welcome():
    """Display a welcoming message to the user."""
    print("\n" + "=" * 60)
    print("🎵 😊 MOOD-BASED MUSIC & ACTIVITY RECOMMENDER 🏃‍♀️ 📚")
    print("=" * 60)
    print("\nHello! Not sure what to do or listen to? I can help!")
    print("Tell me how you're feeling, and I'll recommend music, activities, and quotes.")
    
def get_mood_choice():
    """Present mood options and get user choice."""
    print("\nHow are you feeling today? Choose a mood:")
    
    moods = list(mood_recommendations.keys())
    
    # Display moods in a neat format
    for i, mood in enumerate(moods, 1):
        print(f"{i}. {mood.title()}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of your mood (1-12): "))
            if 1 <= choice <= len(moods):
                return moods[choice-1]
            else:
                print(f"Please enter a number between 1 and {len(moods)}.")
        except ValueError:
            print("Please enter a valid number.")

def display_recommendations(mood):
    """Display recommendations based on the selected mood."""
    recommendations = mood_recommendations[mood]
    
    clear_screen()
    
    print("\n" + "=" * 60)
    print(f"Recommendations for when you're feeling: {mood.upper()}")
    print("=" * 60)
    
    # Display a random playlist recommendation
    playlist = random.choice(recommendations["playlists"])
    print("\n🎵 MUSIC RECOMMENDATION:")
    print(f"Playlist: {playlist}")
    
    # Display a random activity recommendation
    activity = random.choice(recommendations["activities"])
    print("\n🏃‍♀️ ACTIVITY SUGGESTION:")
    print(f"{activity}")
    
    # Display a random quote
    quote = random.choice(recommendations["quotes"])
    print("\n💭 INSPIRATIONAL QUOTE:")
    print(f"{quote}")
    
    print("\n" + "=" * 60)

def see_more_options(mood):
    """Ask if the user wants to see more options for the current mood."""
    while True:
        choice = input("\nWould you like to see more recommendations for this mood? (y/n): ").lower()
        if choice in ['y', 'yes']:
            display_recommendations(mood)
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    """Main function to run the application."""
    clear_screen()
    display_welcome()
    
    while True:
        # Get mood choice from user
        mood = get_mood_choice()
        
        # Display recommendations
        display_recommendations(mood)
        
        # See if they want more recommendations for this mood
        while see_more_options(mood):
            pass
        
        # Ask if they want to check another mood
        while True:
            another = input("\nWould you like to check another mood? (y/n): ").lower()
            if another in ['y', 'yes']:
                clear_screen()
                break
            elif another in ['n', 'no']:
                print("\nThank you for using the Mood Recommender! Have a great day! 😊")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()
