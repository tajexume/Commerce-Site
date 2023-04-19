function draw(x, y){
  const canvas = document.getElementById("canvas");
  if (canvas.getContext) {
    const ctx = canvas.getContext("2d");

    ctx.beginPath();
    ctx.arc(75, 75, 50, 0, Math.PI * 2, true);
    }
    ctx.fillStyle = "rgba(255,255,255,)"
    ctx.fill();
    ctx.stroke();
    ctx.closePath();
}
