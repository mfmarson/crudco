import { Form, redirect } from "react-router-dom";

export async function action({ request }) {
  const formData = await request.formData();
  const userName = formData.get("userName");
  const userPassword = formData.get("userPassword");

  const data = { userName: userName, userPassword: userPassword };

  const Login = await fetch("http://localhost:8000/Login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).then((response) => response.json());
  console.log("Login:", Login);
  return redirect("/Login");
}

const Login  = () => {
  return (
    <Form method="post">
        <h2>Login</h2>
      <label>
        Username
        <input name="userName" type="email" />
      </label>
      <label>
        Password
        <input name="userPassword" type="password" />
      </label>
      <button type="submit">Login</button>
    </Form>
  );
};

export default Login;
