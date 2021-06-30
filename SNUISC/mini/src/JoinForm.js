import React,{useState} from 'react';

const JoinForm =({addMovie}) => {
    const[movieTitle,setMovieTitle] = useState('');
    const[movieYear,setMovieyear] = useState('');
 
    //key는 id역할 서로구분하는
    const resetFrom =() =>{
        setMovieTitle('');
        setMovieyear('');
    };

    const onSubmit=(event) =>{
      event.preventDefault();
      addMovie({
          title: movieTitle,
          year: movieYear,
      });
      resetFrom();

    };
    
    

    return (

    <form onSubmit ={onSubmit}>
        <input
        type="text"
        value={movieTitle}
        placeholder="아이디"
        onChange = {e => setMovieTitle(e.target.value)}
        /><br/>



        <input
        type="text"
        value={movieYear}
        placeholder="비밀번호"
        onChange = {e => setMovieyear(e.target.value)}
        /><br/>

        <button type="submit">회원가입</button>

    </form>

      
    );

};

export default JoinForm;