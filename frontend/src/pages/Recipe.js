import React, {useState} from "react";
import "./Recipe.css";

const Recipe = () => {
  const [isFlipped, setIsFlipped] = useState(false);

  const handleButtonClick = () => {
    setIsFlipped(!isFlipped);
  };

  return (
  <div class="page-wrapper">
    <div class="main-wrapper">
      <div id="recipe-box" className={`recipe-wrapper ${isFlipped ? 'flipped' : ''}`}>
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
          <button class="reroll" onClick={handleButtonClick}>
              <span>REROLL</span>
          </button>
      </div>
    </div>
    
    
    
  </div>);
};

export default Recipe;