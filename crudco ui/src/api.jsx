// import { redirect } from "react-router-dom";

// const API_URL = "http://localhost:8000";

// // Function to get the list of URLs from the backend
// export const getUrls = async () => {
//   const response = await fetch(`${API_URL}/url-list`);
//   if (!response.ok) {
//     throw new Error("Failed to fetch URLs");
//   }
//   return await response.json();
// };

// // Function to add a new URL to the backend
// export const AddUrl = async (data) => {
//   try {
//     const response = await fetch(`http://localhost:8000/add-url`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(data),
//     });

//     const result = await response.json();
//     console.log("ADD URL RESPONSE:", result);

//     return redirect("/add-url");
//   } catch (error) {
//     console.error("Error adding URL:", error);
//   }
// };

// // Function to add a new user to the backend
// export const AddUser = async (data) => {
//   try {
//     const response = await fetch(`http://localhost:8000/add-user`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(data),
//     });

//     const result = await response.json();
//     console.log("ADD USER RESPONSE:", result);

//     return redirect("/add-user");
//   } catch (error) {
//     console.error("Error adding user:", error);
//   }
// };
