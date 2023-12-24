### Challenge 1: Todo List

**Task:** Implement a simple todo list application in React.

**Answer:**
```jsx
import React, { useState } from 'react';

const TodoList = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  const addTodo = () => {
    setTodos([...todos, { id: todos.length + 1, text: newTodo, completed: false }]);
    setNewTodo('');
  };

  const toggleTodo = (id) => {
    setTodos(
      todos.map((todo) =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    );
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter((todo) => todo.id !== id));
  };

  return (
    <div>
      <h2>Todo List</h2>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            {todo.text}
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <div>
        <input
          type="text"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
        />
        <button onClick={addTodo}>Add Todo</button>
      </div>
    </div>
  );
};

export default TodoList;
```

### Challenge 2: Pagination Component

**Task:** Create a reusable pagination component in React.

**Answer:**
```jsx
import React, { useState } from 'react';

const Pagination = ({ totalItems, itemsPerPage, onPageChange }) => {
  const totalPages = Math.ceil(totalItems / itemsPerPage);
  const [currentPage, setCurrentPage] = useState(1);

  const handlePageChange = (page) => {
    setCurrentPage(page);
    onPageChange(page);
  };

  return (
    <div>
      <button
        disabled={currentPage === 1}
        onClick={() => handlePageChange(currentPage - 1)}
      >
        Previous
      </button>
      {Array.from({ length: totalPages }, (_, index) => (
        <button
          key={index + 1}
          onClick={() => handlePageChange(index + 1)}
          disabled={currentPage === index + 1}
        >
          {index + 1}
        </button>
      ))}
      <button
        disabled={currentPage === totalPages}
        onClick={() => handlePageChange(currentPage + 1)}
      >
        Next
      </button>
    </div>
  );
};

export default Pagination;
```


Certainly! Let's continue with a few more challenges along with detailed answers.

### Challenge 3: Image Gallery

**Task:** Build an image gallery component in React. Fetch a list of images from an API and display them in a grid. Include a modal or lightbox feature that allows users to view a larger version of each image.

**Answer:**
```jsx
import React, { useState, useEffect } from 'react';

const ImageGallery = () => {
  const [images, setImages] = useState([]);
  const [selectedImage, setSelectedImage] = useState(null);

  useEffect(() => {
    // Fetch images from an API (replace with your API endpoint)
    const fetchImages = async () => {
      try {
        const response = await fetch('https://example.com/api/images');
        const data = await response.json();
        setImages(data);
      } catch (error) {
        console.error('Error fetching images:', error);
      }
    };

    fetchImages();
  }, []);

  const openModal = (image) => {
    setSelectedImage(image);
  };

  const closeModal = () => {
    setSelectedImage(null);
  };

  return (
    <div>
      <h2>Image Gallery</h2>
      <div className="image-grid">
        {images.map((image) => (
          <img
            key={image.id}
            src={image.url}
            alt={image.description}
            onClick={() => openModal(image)}
          />
        ))}
      </div>
      {selectedImage && (
        <div className="modal">
          <button onClick={closeModal}>Close</button>
          <img src={selectedImage.url} alt={selectedImage.description} />
          <p>{selectedImage.description}</p>
        </div>
      )}
    </div>
  );
};

export default ImageGallery;
```

### Challenge 4: Autocomplete Search

**Task:** Develop an autocomplete search component. Fetch a list of items from an API as the user types and display matching results. Allow the user to select an item from the suggestions.

**Answer:**
```jsx
import React, { useState, useEffect } from 'react';

const AutocompleteSearch = () => {
  const [query, setQuery] = useState('');
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    // Fetch suggestions from an API (replace with your API endpoint)
    const fetchSuggestions = async () => {
      try {
        const response = await fetch(`https://example.com/api/search?q=${query}`);
        const data = await response.json();
        setSuggestions(data);
      } catch (error) {
        console.error('Error fetching suggestions:', error);
      }
    };

    fetchSuggestions();
  }, [query]);

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSelectSuggestion = (suggestion) => {
    setQuery(suggestion);
    setSuggestions([]);
  };

  return (
    <div>
      <h2>Autocomplete Search</h2>
      <input
        type="text"
        value={query}
        onChange={handleInputChange}
        placeholder="Search..."
      />
      <ul>
        {suggestions.map((suggestion) => (
          <li key={suggestion} onClick={() => handleSelectSuggestion(suggestion)}>
            {suggestion}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AutocompleteSearch;
```


Absolutely! Let's continue with a few more coding challenges:

### Challenge 5: Drag and Drop File Upload

**Task:** Implement a file upload component that allows users to drag and drop files to upload. Display a list of uploaded files with the ability to remove them.

**Answer:**
```jsx
import React, { useState } from 'react';

const DragAndDropUpload = () => {
  const [uploadedFiles, setUploadedFiles] = useState([]);

  const handleDrop = (event) => {
    event.preventDefault();
    const newFiles = Array.from(event.dataTransfer.files);
    setUploadedFiles([...uploadedFiles, ...newFiles]);
  };

  const handleRemoveFile = (index) => {
    const updatedFiles = [...uploadedFiles];
    updatedFiles.splice(index, 1);
    setUploadedFiles(updatedFiles);
  };

  return (
    <div
      onDrop={handleDrop}
      onDragOver={(event) => event.preventDefault()}
      style={{ border: '1px dashed #ccc', padding: '20px', margin: '20px' }}
    >
      <h2>Drag and Drop File Upload</h2>
      <div>
        {uploadedFiles.map((file, index) => (
          <div key={index}>
            {file.name}
            <button onClick={() => handleRemoveFile(index)}>Remove</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DragAndDropUpload;
```

### Challenge 6: Social Media Feed

**Task:** Build a social media feed component that displays posts from different users. Include features like liking posts, commenting, and displaying the number of likes and comments.

**Answer:**
```jsx
import React, { useState } from 'react';

const SocialMediaFeed = () => {
  const [posts, setPosts] = useState([
    { id: 1, user: 'User1', content: 'This is post 1', likes: 10, comments: 5 },
    { id: 2, user: 'User2', content: 'This is post 2', likes: 15, comments: 8 },
  ]);

  const handleLike = (postId) => {
    setPosts((prevPosts) =>
      prevPosts.map((post) =>
        post.id === postId ? { ...post, likes: post.likes + 1 } : post
      )
    );
  };

  const handleComment = (postId, comment) => {
    setPosts((prevPosts) =>
      prevPosts.map((post) =>
        post.id === postId
          ? { ...post, comments: post.comments + 1, latestComment: comment }
          : post
      )
    );
  };

  return (
    <div>
      <h2>Social Media Feed</h2>
      {posts.map((post) => (
        <div key={post.id}>
          <p>{post.user}: {post.content}</p>
          <button onClick={() => handleLike(post.id)}>Like ({post.likes})</button>
          <button onClick={() => handleComment(post.id, 'A new comment')}>
            Comment ({post.comments})
          </button>
          {post.latestComment && <p>Latest Comment: {post.latestComment}</p>}
        </div>
      ))}
    </div>
  );
};

export default SocialMediaFeed;
```

Feel free to use and modify these examples based on your project requirements. If you have specific challenges in mind or need more examples, let me know!


Certainly! Let's continue with a few more coding challenges:

### Challenge 7: Recipe Book

**Task:** Create a recipe book application where users can view a list of recipes, search for recipes, and view details about each recipe. Include a feature for adding new recipes.

**Answer:**
```jsx
import React, { useState } from 'react';

const RecipeBook = () => {
  const [recipes, setRecipes] = useState([
    { id: 1, title: 'Pasta Carbonara', ingredients: ['Pasta', 'Eggs', 'Bacon', 'Parmesan'] },
    { id: 2, title: 'Chicken Stir-Fry', ingredients: ['Chicken', 'Vegetables', 'Soy Sauce'] },
  ]);

  const [newRecipe, setNewRecipe] = useState({ title: '', ingredients: [] });

  const addRecipe = () => {
    setRecipes([...recipes, { id: recipes.length + 1, ...newRecipe }]);
    setNewRecipe({ title: '', ingredients: [] });
  };

  return (
    <div>
      <h2>Recipe Book</h2>
      <ul>
        {recipes.map((recipe) => (
          <li key={recipe.id}>
            <strong>{recipe.title}</strong>
            <ul>
              {recipe.ingredients.map((ingredient, index) => (
                <li key={index}>{ingredient}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
      <div>
        <h3>Add a New Recipe</h3>
        <label>Title: <input type="text" value={newRecipe.title} onChange={(e) => setNewRecipe({ ...newRecipe, title: e.target.value })} /></label>
        <label>Ingredients: <input type="text" value={newRecipe.ingredients.join(',')} onChange={(e) => setNewRecipe({ ...newRecipe, ingredients: e.target.value.split(',') })} /></label>
        <button onClick={addRecipe}>Add Recipe</button>
      </div>
    </div>
  );
};

export default RecipeBook;
```

### Challenge 8: Currency Converter

**Task:** Build a currency converter application using React. Allow users to select currencies, enter an amount, and view the converted amount based on real-time exchange rates.

**Answer:**
```jsx
import React, { useState, useEffect } from 'react';

const CurrencyConverter = () => {
  const [currencies, setCurrencies] = useState([]);
  const [amount, setAmount] = useState(1);
  const [fromCurrency, setFromCurrency] = useState('USD');
  const [toCurrency, setToCurrency] = useState('EUR');
  const [convertedAmount, setConvertedAmount] = useState(null);

  useEffect(() => {
    // Fetch currency rates from an API (replace with your API endpoint)
    const fetchCurrencies = async () => {
      try {
        const response = await fetch('https://example.com/api/currencies');
        const data = await response.json();
        setCurrencies(data);
      } catch (error) {
        console.error('Error fetching currencies:', error);
      }
    };

    fetchCurrencies();
  }, []);

  useEffect(() => {
    // Fetch real-time exchange rates from an API (replace with your API endpoint)
    const fetchExchangeRate = async () => {
      try {
        const response = await fetch(`https://example.com/api/exchange-rate?from=${fromCurrency}&to=${toCurrency}`);
        const data = await response.json();
        setConvertedAmount(amount * data.rate);
      } catch (error) {
        console.error('Error fetching exchange rate:', error);
      }
    };

    fetchExchangeRate();
  }, [fromCurrency, toCurrency, amount]);

  return (
    <div>
      <h2>Currency Converter</h2>
      <label>
        Amount: <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} />
      </label>
      <label>
        From Currency:
        <select value={fromCurrency} onChange={(e) => setFromCurrency(e.target.value)}>
          {currencies.map((currency) => (
            <option key={currency} value={currency}>
              {currency}
            </option>
          ))}
        </select>
      </label>
      <label>
        To Currency:
        <select value={toCurrency} onChange={(e) => setToCurrency(e.target.value)}>
          {currencies.map((currency) => (
            <option key={currency} value={currency}>
              {currency}
            </option>
          ))}
        </select>
      </label>
      <p>Converted Amount: {convertedAmount}</p>
    </div>
  );
};

export default CurrencyConverter;
```

Feel free to adapt and modify these examples based on your project requirements. If you have specific challenges in mind or need more examples, let me know!


Certainly! Let's proceed with a couple more coding challenges:

### Challenge 9: Notification Component

**Task:** Develop a reusable notification component. Users should be able to trigger different types of notifications (success, error, info) with custom messages.

**Answer:**
```jsx
import React, { useState } from 'react';

const Notification = ({ type, message }) => {
  const [visible, setVisible] = useState(true);

  const handleClose = () => {
    setVisible(false);
  };

  return (
    <div style={{ display: visible ? 'block' : 'none', padding: '10px', border: '1px solid', marginBottom: '10px', backgroundColor: getBackgroundColor(type) }}>
      <p>{message}</p>
      <button onClick={handleClose}>Close</button>
    </div>
  );
};

const getBackgroundColor = (type) => {
  switch (type) {
    case 'success':
      return '#4CAF50';
    case 'error':
      return '#f44336';
    case 'info':
      return '#2196F3';
    default:
      return '#ddd';
  }
};

// Example usage:
// <Notification type="success" message="Operation successful!" />
// <Notification type="error" message="Operation failed!" />
// <Notification type="info" message="Informational message" />
```

### Challenge 10: Music Player

**Task:** Build a simple music player component that allows users to play, pause, skip, and adjust the volume of a playlist of songs.

**Answer:**
```jsx
import React, { useState } from 'react';

const MusicPlayer = () => {
  const [playlist, setPlaylist] = useState([
    { id: 1, title: 'Song 1', artist: 'Artist 1', src: 'song1.mp3' },
    { id: 2, title: 'Song 2', artist: 'Artist 2', src: 'song2.mp3' },
  ]);

  const [currentSong, setCurrentSong] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [volume, setVolume] = useState(50);

  const playPause = () => {
    setIsPlaying(!isPlaying);
  };

  const nextSong = () => {
    const currentIndex = playlist.findIndex((song) => song.id === currentSong.id);
    const nextIndex = (currentIndex + 1) % playlist.length;
    setCurrentSong(playlist[nextIndex]);
    setIsPlaying(true);
  };

  const handleVolumeChange = (event) => {
    setVolume(event.target.value);
  };

  return (
    <div>
      <h2>Music Player</h2>
      {currentSong && (
        <div>
          <p>{currentSong.title} - {currentSong.artist}</p>
          <audio
            src={currentSong.src}
            controls
            autoPlay={isPlaying}
            onEnded={nextSong}
            volume={volume / 100}
          />
        </div>
      )}
      <button onClick={playPause}>{isPlaying ? 'Pause' : 'Play'}</button>
      <button onClick={nextSong}>Next</button>
      <label>
        Volume:
        <input type="range" min="0" max="100" value={volume} onChange={handleVolumeChange} />
      </label>
    </div>
  );
};

export default MusicPlayer;
```

Feel free to customize these examples based on your project requirements. If you have specific challenges in mind or need more examples, let me know!

Certainly! Let's continue with a couple more coding challenges:

### Challenge 11: Online Learning Platform

**Task:** Develop a simplified online learning platform with courses and lessons. Users should be able to enroll in courses, view lessons, and track their progress.

**Answer:**
```jsx
import React, { useState } from 'react';

const OnlineLearningPlatform = () => {
  const [courses, setCourses] = useState([
    {
      id: 1,
      title: 'Introduction to React',
      lessons: [
        { id: 1, title: 'Getting Started with React' },
        { id: 2, title: 'Components and Props' },
      ],
    },
    {
      id: 2,
      title: 'Node.js Basics',
      lessons: [
        { id: 1, title: 'Introduction to Node.js' },
        { id: 2, title: 'Building a Simple Server' },
      ],
    },
  ]);

  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const enrollInCourse = (courseId) => {
    setEnrolledCourses([...enrolledCourses, courseId]);
  };

  return (
    <div>
      <h2>Online Learning Platform</h2>
      <h3>Available Courses</h3>
      <ul>
        {courses.map((course) => (
          <li key={course.id}>
            {course.title}
            <button onClick={() => enrollInCourse(course.id)}>Enroll</button>
          </li>
        ))}
      </ul>
      <h3>Enrolled Courses</h3>
      <ul>
        {enrolledCourses.map((courseId) => {
          const course = courses.find((c) => c.id === courseId);
          return (
            <li key={course.id}>
              {course.title}
              <ul>
                {course.lessons.map((lesson) => (
                  <li key={lesson.id}>{lesson.title}</li>
                ))}
              </ul>
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default OnlineLearningPlatform;
```

### Challenge 12: Calculator App

**Task:** Implement a calculator application with basic arithmetic operations. Include features like memory storage and the ability to clear the calculation.

**Answer:**
```jsx
import React, { useState } from 'react';

const CalculatorApp = () => {
  const [displayValue, setDisplayValue] = useState('0');
  const [memory, setMemory] = useState(null);
  const [operator, setOperator] = useState(null);

  const handleNumberClick = (number) => {
    setDisplayValue((prevValue) => (prevValue === '0' ? number : prevValue + number));
  };

  const handleOperatorClick = (selectedOperator) => {
    setMemory(displayValue);
    setOperator(selectedOperator);
    setDisplayValue('0');
  };

  const handleEqualsClick = () => {
    const currentValue = parseFloat(displayValue);
    const memoryValue = parseFloat(memory);

    switch (operator) {
      case '+':
        setDisplayValue((memoryValue + currentValue).toString());
        break;
      case '-':
        setDisplayValue((memoryValue - currentValue).toString());
        break;
      case '*':
        setDisplayValue((memoryValue * currentValue).toString());
        break;
      case '/':
        setDisplayValue((memoryValue / currentValue).toString());
        break;
      default:
        break;
    }

    setMemory(null);
    setOperator(null);
  };

  const handleClearClick = () => {
    setDisplayValue('0');
    setMemory(null);
    setOperator(null);
  };

  return (
    <div>
      <h2>Calculator App</h2>
      <div>
        <p>{displayValue}</p>
        <button onClick={handleClearClick}>C</button>
        <button onClick={() => handleNumberClick('7')}>7</button>
        <button onClick={() => handleNumberClick('8')}>8</button>
        <button onClick={() => handleNumberClick('9')}>9</button>
        <button onClick={() => handleOperatorClick('/')}>/</button>
      </div>
      {/* Other number and operator buttons */}
      <div>
        <button onClick={() => handleEqualsClick()}>=</button>
      </div>
    </div>
  );
};

export default CalculatorApp;
```

Feel free to adapt and modify these examples based on your project requirements. If you have specific challenges in mind or need more examples, let me know!

Certainly! Let's continue with a couple more coding challenges:

### Challenge 13: Countdown Timer

**Task:** Create a countdown timer component. Allow users to set a timer for a specific duration and display the countdown in real-time.

**Answer:**
```jsx
import React, { useState, useEffect } from 'react';

const CountdownTimer = () => {
  const [duration, setDuration] = useState(0);
  const [timer, setTimer] = useState(null);

  const handleInputChange = (event) => {
    setDuration(event.target.value);
  };

  const startTimer = () => {
    setTimer(setInterval(() => {
      setDuration((prevDuration) => {
        if (prevDuration === 0) {
          clearInterval(timer);
          setTimer(null);
          return 0;
        }
        return prevDuration - 1;
      });
    }, 1000));
  };

  const stopTimer = () => {
    clearInterval(timer);
    setTimer(null);
  };

  useEffect(() => {
    return () => {
      if (timer) {
        clearInterval(timer);
      }
    };
  }, [timer]);

  return (
    <div>
      <h2>Countdown Timer</h2>
      <label>
        Set Timer (seconds): <input type="number" value={duration} onChange={handleInputChange} />
      </label>
      <div>
        <button onClick={startTimer}>Start</button>
        <button onClick={stopTimer}>Stop</button>
      </div>
      <p>Time Remaining: {duration} seconds</p>
    </div>
  );
};

export default CountdownTimer;
```

### Challenge 14: Portfolio Website

**Task:** Build your personal portfolio website using React. Include sections for projects, skills, and a contact form.

**Answer:**
```jsx
import React from 'react';

const PortfolioWebsite = () => {
  return (
    <div>
      <h2>My Portfolio</h2>
      <section>
        <h3>Projects</h3>
        <ul>
          <li>
            <strong>Project 1</strong>
            <p>Description of Project 1.</p>
          </li>
          <li>
            <strong>Project 2</strong>
            <p>Description of Project 2.</p>
          </li>
        </ul>
      </section>
      <section>
        <h3>Skills</h3>
        <ul>
          <li>React</li>
          <li>JavaScript</li>
          <li>HTML/CSS</li>
          {/* Add more skills */}
        </ul>
      </section>
      <section>
        <h3>Contact</h3>
        <form>
          <label>
            Name: <input type="text" />
          </label>
          <label>
            Email: <input type="email" />
          </label>
          <label>
            Message: <textarea />
          </label>
          <button type="submit">Send Message</button>
        </form>
      </section>
    </div>
  );
};

export default PortfolioWebsite;
```

Feel free to customize these examples based on your project requirements. If you have specific challenges in mind or need more examples, let me know!

Certainly! Let's continue with a couple more coding challenges:

### Challenge 15: Image Slider

**Task:** Build an image slider component in React. Users should be able to navigate through a series of images, and the slider should loop back to the beginning after reaching the last image.

**Answer:**
```jsx
import React, { useState } from 'react';

const ImageSlider = ({ images }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const goToNextImage = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  const goToPreviousImage = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
  };

  return (
    <div>
      <h2>Image Slider</h2>
      <div>
        <button onClick={goToPreviousImage}>Previous</button>
        <img src={images[currentIndex]} alt={`Image ${currentIndex + 1}`} />
        <button onClick={goToNextImage}>Next</button>
      </div>
    </div>
  );
};

export default ImageSlider;
```

### Challenge 16: Weather App

**Task:** Develop a simple weather application using a weather API. Users should be able to enter a city and view the current weather conditions.

**Answer:**
```jsx
import React, { useState } from 'react';

const WeatherApp = () => {
  const [city, setCity] = useState('');
  const [weatherData, setWeatherData] = useState(null);

  const fetchWeatherData = async () => {
    try {
      const response = await fetch(`https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=${city}`);
      const data = await response.json();
      setWeatherData(data);
    } catch (error) {
      console.error('Error fetching weather data:', error);
    }
  };

  const handleCityChange = (event) => {
    setCity(event.target.value);
  };

  const handleSearch = () => {
    fetchWeatherData();
  };

  return (
    <div>
      <h2>Weather App</h2>
      <label>
        Enter City: <input type="text" value={city} onChange={handleCityChange} />
      </label>
      <button onClick={handleSearch}>Search</button>
      {weatherData && (
        <div>
          <h3>{weatherData.location.name}, {weatherData.location.country}</h3>
          <p>Temperature: {weatherData.current.temp_c}°C</p>
          <p>Condition: {weatherData.current.condition.text}</p>
          {/* Add more weather information */}
        </div>
      )}
    </div>
  );
};

export default WeatherApp;
```

Make sure to replace `'YOUR_API_KEY'` in the Weather App example with your actual API key from a weather service provider.

Feel free to adapt and modify these examples based on your project requirements. If you have specific challenges in mind or need more examples, let me know!


Certainly! Let's provide a detailed example with answers for the GitHub Profile Viewer challenge. In this example, we'll create a simple React app that allows users to enter a GitHub username, fetches the user's profile information and repositories, and displays them.

```jsx
// GitHubProfileViewer.jsx

import React, { useState } from 'react';

const GitHubProfileViewer = () => {
  const [username, setUsername] = useState('');
  const [profile, setProfile] = useState(null);
  const [repositories, setRepositories] = useState([]);

  const fetchGitHubData = async () => {
    try {
      // Fetch user profile data
      const profileResponse = await fetch(`https://api.github.com/users/${username}`);
      const profileData = await profileResponse.json();
      setProfile(profileData);

      // Fetch user repositories
      const repositoriesResponse = await fetch(`https://api.github.com/users/${username}/repos`);
      const repositoriesData = await repositoriesResponse.json();
      setRepositories(repositoriesData);
    } catch (error) {
      console.error('Error fetching GitHub data:', error);
    }
  };

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handleSearch = () => {
    fetchGitHubData();
  };

  return (
    <div>
      <h2>GitHub Profile Viewer</h2>
      <label>
        Enter GitHub Username: <input type="text" value={username} onChange={handleUsernameChange} />
      </label>
      <button onClick={handleSearch}>Search</button>

      {profile && (
        <div>
          <h3>{profile.name}</h3>
          <img src={profile.avatar_url} alt="User Avatar" />
          <p>{profile.bio}</p>
        </div>
      )}

      {repositories.length > 0 && (
        <div>
          <h3>Repositories</h3>
          <ul>
            {repositories.map((repo) => (
              <li key={repo.id}>
                <strong>{repo.name}</strong>
                <p>{repo.description}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default GitHubProfileViewer;
```

In this example:

- The `useState` hook is used to manage the state of the username, user profile, and repositories.
- The `fetchGitHubData` function is an asynchronous function that uses the `fetch` API to make requests to the GitHub API and update the state accordingly.
- The `handleUsernameChange` function updates the `username` state as the user types in the input field.
- The `handleSearch` function triggers the GitHub data fetch when the user clicks the "Search" button.
- The rendered JSX displays the user's profile information and a list of repositories if available.

You can integrate this component into your React application and further enhance it based on your specific requirements.


