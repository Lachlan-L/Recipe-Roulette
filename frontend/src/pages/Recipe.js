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
const [isFlipped, setIsFlipped] = useState(false);

  const handleButtonClick = () => {
    setIsFlipped(!isFlipped);
  };

  return (
  <div class="page-wrapper">
  <div class="main-wrapper">
    <div id="recipe-box" class="recipe-wrapper">
        <div class="title-wrapper">
            Title Placeholder
        </div>
        <div class="image-wrapper">
            <div>
                Image Placeholder
            </div>
        </div>
        <div class="ingredients-wrapper">
            <div>
                Ingredients Placeholder
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