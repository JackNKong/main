import React, { useState } from 'react';
import Movie from './Movie';
import MovieForm from './JoinForm';





function App() {
  const [movies, setMovies] = useState([
    { title: 'abc@naver.com', year: 1234},
    { title: 'abc@gmail.com', year: 1234},
    { title: 'efg_abcd@.gmail.com', year: 204503},
    { title: 'efff@naver.com', year: 20513104}
  ]);

  const renderMovies = movies.map(movie => {
    return (
      <Movie movie={movie} key={movie.title}/>
    );
  });



  const addMovie = (movie) => {
    setMovies([
      ...movies,
      movie
    ]);
  };
  return (
    <div className="App">
      <h1>회원가입하기</h1>
      <MovieForm addMovie={addMovie} />
      {renderMovies}
      {/* //{movies} */}
    </div>
  );

  
}




export default App;