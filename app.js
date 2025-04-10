// Main application logic
document.addEventListener('DOMContentLoaded', () => {
    const moodButtons = document.querySelectorAll('.mood-btn');
    const recommendationsContainer = document.getElementById('recommendations');
    const moodTitle = document.getElementById('mood-title');
    const playlistRecommendation = document.getElementById('playlist-recommendation');
    const activityRecommendation = document.getElementById('activity-recommendation');
    const quoteRecommendation = document.getElementById('quote-recommendation');
    const refreshBtn = document.getElementById('refresh-btn');
    const backBtn = document.getElementById('back-btn');
    
    // Store current mood
    let currentMood = '';
    
    // Data objects for each mood type
    const moodData = {
        playlists: {},
        activities: {},
        quotes: {}
    };
    
    // Load all CSV data when the app starts
    loadAllCSVData();
    
    // Event listener for mood buttons
    moodButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentMood = button.getAttribute('data-mood');
            showRecommendations(currentMood);
        });
    });
    
    // Refresh button - show new recommendations for the same mood
    refreshBtn.addEventListener('click', () => {
        showRecommendations(currentMood);
    });
    
    // Back button - return to mood selection
    backBtn.addEventListener('click', () => {
        recommendationsContainer.style.display = 'none';
        document.querySelector('.mood-selection').style.display = 'block';
    });
    
    // Function to load all CSV data
    async function loadAllCSVData() {
        try {
            const moods = [
                'happy', 'sad', 'energetic', 'needs-uplifting', 
                'post-breakup', 'angry', 'tired', 'love-songs', 
                'stressed', 'bored', 'exercise', 'sporty'
            ];
            
            for (const mood of moods) {
                // Load playlists, activities, and quotes for each mood
                moodData.playlists[mood] = await loadCSV(`data/${mood}_playlists.csv`);
                moodData.activities[mood] = await loadCSV(`data/${mood}_activities.csv`);
                moodData.quotes[mood] = await loadCSV(`data/${mood}_quotes.csv`);
            }
            
            // Once data is loaded, enable buttons
            enableMoodButtons();
            
        } catch (error) {
            console.error('Error loading CSV data:', error);
            alert('There was an error loading recommendation data. Please try again later.');
        }
    }
    
    // Function to load a single CSV file
    async function loadCSV(filepath) {
        try {
            const response = await fetch(filepath);
            if (!response.ok) {
                throw new Error(`Failed to load ${filepath}: ${response.status} ${response.statusText}`);
            }
            
            const csvText = await response.text();
            // Parse CSV rows (assuming simple CSV with one value per line)
            return csvText.split('\n')
                .filter(line => line.trim() !== '')
                .map(line => line.trim());
                
        } catch (error) {
            console.error(`Error loading ${filepath}:`, error);
            // Return some fallback data if CSV loading fails
            return ['Data unavailable. Please try again later.'];
        }
    }
    
    // Function to enable mood buttons after data is loaded
    function enableMoodButtons() {
        moodButtons.forEach(button => {
            button.disabled = false;
        });
    }
    
    // Function to show recommendations based on mood
    function showRecommendations(mood) {
        // Format the mood name for display
        const formattedMood = mood.replace(/-/g, ' ');
        moodTitle.textContent = `Recommendations for when you're feeling: ${formattedMood.toUpperCase()}`;

        // Reset animation by removing classes and re-adding them after a tiny delay
    const boxes = document.querySelectorAll('.recommendation-box');
    boxes.forEach(box => {
        box.style.animation = 'none';
        box.offsetHeight; // Trigger reflow
    }];    
        
        // Get random recommendations
        const playlist = getRandomItem(moodData.playlists[mood]);
        const activity = getRandomItem(moodData.activities[mood]);
        const quote = getRandomItem(moodData.quotes[mood]);
        
        // Update the recommendation text
        playlistRecommendation.textContent = playlist;
        activityRecommendation.textContent = activity;
        quoteRecommendation.textContent = quote;
        
        // Re-enable animations after content is updated
        setTimeout(() => {
            boxes.forEach(box => {
                box.style.animation = '';
            });
        }, 10);
        
        // Hide mood selection, show recommendations
        document.querySelector('.mood-selection').style.display = 'none';
        recommendationsContainer.style.display = 'block';
        
        // Reset animation by removing and re-adding recommendation boxes
       // const boxes = document.querySelectorAll('.recommendation-box');
        //boxes.forEach(box => {
          //  const clone = box.cloneNode(true);
           // box.parentNode.replaceChild(clone, box);
       // });
    }
    
    // Helper function to get a random item from an array
    function getRandomItem(array) {
        if (!array || array.length === 0) {
            return 'Recommendation not available';
        }
        const randomIndex = Math.floor(Math.random() * array.length);
        return array[randomIndex];
    }
});
