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
import { useNavigate } from "react-router-dom";
import './bubble-right.css';

const options = ['Vegetables', 'Seafood', 'Fruit', 'Meat'];
const imageOptions = [banana, grape, pumpkin, meat, carrot, steak, chicken, fish, apple];

const Roulette = () => {
  const [selections, setSelections] = useState(Array(3).fill('Vegetables'));
  const [images, setImages] = useState(Array(3).fill(apple));
  const [clicked, setClicked] = useState(false);
  const navigate = useNavigate();

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
          return imageOptions[Math.floor(Math.random() * imageOptions.length)];
        }
        return img;
      }));
  
      counter++;
      if (counter > 10) {
        clearInterval(interval);
        setImages((currentImages) => currentImages.map((img, i) => {
          if (i === index) {
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
    navigate('/recipe');
  }

  return (
    <div className="page">
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
        <button onClick={handleSpinAll} className="spinButton btn-22 spinType"><span>Spin All</span></button>
        {clicked &&<button onClick={recipe} className="btn-22 recipeButton recipeType"><span>Find Recipe</span></button>}
      </div>
    </div>
  );
};

export default Roulette;