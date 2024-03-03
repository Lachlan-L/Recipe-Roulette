import React, { useState, useEffect } from 'react'
import "./Recipe.css";

const Recipe = () => {
  const [data, setData] = useState([{}])

  useEffect(() => {
    const savedData = JSON.parse(localStorage.getItem('ingredients'));
    const queryParam = savedData[0] + '+' + savedData[1] + '+' + savedData[2];
    queryParam.replace(' ', '+');
    fetchData(queryParam);
  }, []);

  const fetchData = async (queryParam) => {
      const response = await fetch(`/get-recipe-details?ingredients=${queryParam}`);
      const responseData = await response.json();
      setData(responseData);
  };

  const [isFlipped, setIsFlipped] = useState(false);

  const handleButtonClick = () => {
    setIsFlipped(!isFlipped);
    fetchData();
  };

  return (
  <div class="page-wrapper">
    <div class="main-wrapper">
      <div id="recipe-box" className={`recipe-wrapper ${isFlipped ? 'flipped' : ''}`}>
          <div class="title-wrapper">
            {(typeof data.title === 'undefined') ? (
              <p>Loading...</p>
            ) : (
              <h2 class = 'recipeTitle'>{data.title}</h2>
            )}
          </div>
          <div class="image-wrapper">
              <div>
                {(typeof data.image === 'undefined') ? (
                  <p>Loading...</p>
                ) : (
                  <img src={data.image} alt={data.title} className="imageStyle" />
                )}
              </div>
          </div>
          <div class="ingredients-wrapper">
              <div>
                <p class='ingredientList'>Ingredient List</p>
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