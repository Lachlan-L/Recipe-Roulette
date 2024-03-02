import React from "react";
import "./Recipe.css";

const Recipe = () => {
  
  function handleClick() {
    document.getElementById('recipe-box').style = 'transform: rotate()'
  }
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
        <button>
            <p>REROLL</p>
        </button>
    </div>
  </div>
    
    
  </div>);
};

export default Recipe;