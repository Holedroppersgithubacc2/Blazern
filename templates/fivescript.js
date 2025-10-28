function startBoost(type) {
    const boostInput = document.getElementById("boost-input");
    const boostTitle = document.getElementById("boost-title");
    const boostText = document.getElementById("boost-text");
  
    boostInput.style.display = "block"; 
  
    if (type === 'brain') {
      boostTitle.innerText = "Brain Dump";
      boostText.placeholder = "Write down everything on your mind...";
    } else if (type === 'goal') {
      boostTitle.innerText = "Set a Goal";
      boostText.placeholder = "What’s one thing you want to accomplish?";
    } else if (type === 'reset') {
      boostTitle.innerText = "Mental Reset";
      boostText.placeholder = "Take a deep breath. Write how you're feeling right now.";
    }
  
    boostText.value = "";
  }
  
