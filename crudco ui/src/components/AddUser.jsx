import { Form, redirect } from "react-router-dom";

export async function action({ request }) {
  const formData = await request.formData();
  const userName = formData.get("userName");
  const userPassword = formData.get("userPassword");

  const data = { username: userName, hashed_password: userPassword };

  const addUser = await fetch("http://localhost:8000/add-user", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).then((response) => response.json());
  console.log("User Added:", addUser);
  return redirect("add-user");
}

const addUser = () => {
  return (
    <Form method="post">
      <h2>Add User</h2>
      <label>
        Username (email)
        <input name="userName" type="email" />
      </label>
      <label>
        Password
        <input name="userPassword" type="password" />
      </label>
      <button type="submit">Submit User</button>
    </Form>
  );
};

export default addUser;
