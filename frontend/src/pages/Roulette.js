import React, { useState } from "react";
import './Roulette.css';
import apple from './assets/apple.png';
import banana from "./assets/banana.png";
import grape from "./assets/grape.png";
import pumpkin from "./assets/pumpkin.png";
import meat from "./assets/meat.png";
import carrot from "./assets/carrot.png";
import steak from "./assets/steak.png";
import chicken from "./assets/chicken.png";
import fish from "./assets/fish.png";

const options = ['Vegetables', 'Seafood', 'Fruit', 'Meat'];
const imageOptions = [banana, grape, pumpkin, meat, carrot, steak, chicken, fish, apple];

const Roulette = () => {
  const [selections, setSelections] = useState(Array(3).fill('Vegetables'));
  const [images, setImages] = useState(Array(3).fill(apple));
  const [clicked, setClicked] = useState(false);

  const handleSpinAll = () => {
    setClicked(true);
    for (let index = 0; index < images.length; index++) {
      handleReroll(index);
    }
  };

  const handleReroll = (index) => {
    let counter = 0;
    const interval = setInterval(() => {
      setImages((currentImages) => currentImages.map((img, i) => {
        if (i === index) {
          // Return a new random image for the current slot
          return imageOptions[Math.floor(Math.random() * imageOptions.length)];
        }
        return img;
      }));
  
      counter++;
      if (counter > 10) {
        clearInterval(interval);
        // Optionally reset the slot to a specific image after spinning
        setImages((currentImages) => currentImages.map((img, i) => {
          if (i === index) {
            // This could be adjusted to set a specific image after spinning
            // For now, it randomly selects a new image to simulate a final spin result
            return imageOptions[Math.floor(Math.random() * imageOptions.length)];
          }
          return img;
        }));
      }
    }, 100);
  };

  const setSelection = (value, index) => {
    setSelections(choices => 
      choices.map((item, i) => i === index ? value : item)
    );
  }

  const recipe = () => {

  }

  return (
    <div className="container">
      <h1 className="title">Test Your Luck</h1>
      <div className="box-row">
        {images.map((imageSrc, index) => (
          <div key={index} className="box-container">
            <div className="box">
              <img src={imageSrc} alt={`Slot ${index}`} />
            </div>
            {clicked && <button className="rerollButton" onClick={() => handleReroll(index)}>Reroll</button>}
            <div class="select-wrapper">
            <select class="drop-down" value={selections[index]} onChange={e => setSelection(e.target.value, index)}>
              {options.map(option => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
          </div>
          </div>
        ))}
      </div>
      <button onClick={handleSpinAll} className="spinButton">Spin All</button>
      {clicked &&<button onClick={recipe} className="recipeButton">Find Recipe</button>}
    </div>
  );
};

export default Roulette;