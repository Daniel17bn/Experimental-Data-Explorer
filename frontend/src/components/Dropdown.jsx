import React, { useState } from 'react';

// Importing React and the useState hook.
// React is the library we use to build components, and useState is a hook that allows us to manage state in functional components.

const Dropdown = () => {
  // Declaring a functional component named Dropdown.

  const [selectedOption, setSelectedOption] = useState('');
  // Declaring a state variable `selectedOption` with an initial value of an empty string.
  // `setSelectedOption` is the function used to update the value of `selectedOption`.

  const handleChange = (event) => {
    setSelectedOption(event.target.value);
  };
  // Defining a function `handleChange` that will be triggered when the dropdown value changes.
  // `event.target.value` gets the value of the selected option, and `setSelectedOption` updates the state.

  return (
    <div>
      {/* A container div to hold the dropdown and any related content. */}
      <label htmlFor="dropdown">Choose an option:</label>
      {/* A label for accessibility, associated with the dropdown via the `htmlFor` attribute. */}
      <select id="dropdown" value={selectedOption} onChange={handleChange}>
        {/* A select element to create the dropdown. */}
        <option value="">--Please choose an option--</option>
        {/* A default option prompting the user to select something. */}
        <option value="option1">Option 1</option>
        {/* An option with the value "option1" and displayed text "Option 1". */}
        <option value="option2">Option 2</option>
        {/* An option with the value "option2" and displayed text "Option 2". */}
        <option value="option3">Option 3</option>
        {/* An option with the value "option3" and displayed text "Option 3". */}
      </select>
      <p>You selected: {selectedOption}</p>
      {/* A paragraph displaying the currently selected option. */}
    </div>
  );
};

export default Dropdown;
// Exporting the Dropdown component so it can be imported and used in other parts of the application.