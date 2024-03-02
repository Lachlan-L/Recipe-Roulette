import React, { useState, useEffect } from 'react'
import "./Recipe.css";

const Recipe = () => {
    const [data, setData] = useState([{}])

    useEffect(() => {
      fetch("/get-recipes").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data)
        }
      )
    }, [])

  function handleClick() {
    document.getElementById('recipe-box').style.color = 'red';
  }

  return (
  <div class="page-wrapper">
  <div class="main-wrapper">
    <div id="recipe-box" class="recipe-wrapper">
        <div class="title-wrapper">
            <div>
                {(typeof data.title === 'undefined') ? (
                    <p>Loading...</p>
                ) : (
                    <h2>{data.title}</h2>
                )}
            </div>
        </div>
        <div class="image-wrapper">
            <div>
                {(typeof data.image === 'undefined') ? (
                    <p>Loading...</p>
                ) : (
                    <img src={data.image} alt="food image"></img>
                )}
            </div>
        </div>
        <div class="ingredients-wrapper">
            <div>
                {(typeof data.ingredients === 'undefined') ? (
                    <p>Loading...</p>
                ) : (
                    <ul>
                        {data.ingredients.map((ingredient, i) => (
                            <li key={i}>{ingredient}</li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    </div>
    <div class="button-wrapper">
        <button onClick={handleClick}>
            <p>REROLL</p>
        </button>
    </div>
  </div>
    
    
  </div>);
};

export default Recipe;