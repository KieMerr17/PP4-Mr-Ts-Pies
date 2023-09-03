// List of all reviews
const reviews = [
    {
      name: "Kieran Merrett",
      review: "Great pies, i absolutely love the beef brisket."
    },
    {
      name: "Mollie Robson",
      review: "Delicious pies, hugely recommended"
    },
    {
      name: "Richard Semple",
      review: "Never fails to please you will not find a better pie I promise."
    },
    {
      name: "Samantha Howells",
      review: "Delicious pies with loads of flavour and very friendly fun professional team."
    },
    {
      name: "Tracy Jamie",
      review: "Beetroot & Stilton Pie is genius! Absolutely loved it"
    },
    {
      name: "Ian Dudley",
      review: "Brilliant pasties, could not fault at all. Highly recommended."
    },
    {
      name: "Elly Charles Taylor",
      review: "Hands down this is the best pie I have ever had. Stilton, celery, garlic & leek"
    },
    {
      name: "Pj Atkinson",
      review: "Highly recommend!! absalouty delicious, quality locally made pies"
    },
    {
      name: "AlKelly Hatfieldex",
      review: "Delicious pies!! Thank you so much, best pie I’ve had in years!"
    },
    {
      name: "Emma Merrett",
      review: "These pies are delicious, i love the vegitarian one he does."
    },
  ];

  
  
// Connect the form elements

  const reviewName = document.getElementById("review-name");
  const reviewText = document.getElementById("review-text");
  const reviewContainer = document.querySelector(".review");
  
  let index = 0;
  
  let previousIndex = -1;

function showReview() {
  let randomIndex = previousIndex;
  while (randomIndex === previousIndex) {
    randomIndex = Math.floor(Math.random() * reviews.length);
  }
  previousIndex = randomIndex;
  
  const { name, review } = reviews[randomIndex];
  reviewName.textContent = ("- ") + name;        // reviewers name
  reviewText.innerHTML = `<em>"  ${review}  "</em>`;   // review
  reviewContainer.classList.add("show");
  
  // time to display
  setTimeout(() => {
    reviewContainer.classList.remove("show");
  }, 6000);
}

showReview();
// time between reviews
setInterval(showReview, 6500);