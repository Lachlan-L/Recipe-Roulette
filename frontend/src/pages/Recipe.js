import React, { useState, useEffect } from 'react'
import "./Recipe.css";

const Recipe = () => {
  const [data, setData] = useState([{}])

    useEffect(() => {
      fetch("/get-recipes-details").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data)
        }
      )
    }, [])

  const [isFlipped, setIsFlipped] = useState(false);

  const handleButtonClick = () => {
    setIsFlipped(!isFlipped);
  };

  return (
  <div class="page-wrapper">
    <div class="main-wrapper">
      <div id="recipe-box" className={`recipe-wrapper ${isFlipped ? 'flipped' : ''}`}>
          <div class="title-wrapper">
            {(typeof data.title === 'undefined') ? (
              <p>Loading...</p>
            ) : (
              <h2>{data.title}</h2>
            )}
          </div>
          <div class="image-wrapper">
              <div>
                {(typeof data.image === 'undefined') ? (
                  <p>Loading...</p>
                ) : (
                  <img src={data.image} alt={data.title} />
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
          <button class="reroll" onClick={handleButtonClick}>
              <span>REROLL</span>
          </button>
      </div>
    </div>
  </div>);
};

export default Recipe;