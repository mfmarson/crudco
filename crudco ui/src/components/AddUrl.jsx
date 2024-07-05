import { Form, redirect } from "react-router-dom";

export async function action({ request }) {
  const formData = await request.formData();
  const long_url = formData.get("long_url");
  const title = formData.get("title");

  const data = { long_url: long_url, title: title };
  const addUrl = await fetch("http://localhost:8000/add-url", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).then((response) => response.json());
  console.log("Shrink URL:", addUrl);
  return redirect("/add-url");
}

const AddUrl = () => {
  return (
    <>
      <Form method="post">
        <h2>Add URL</h2>
        <label>
          Original (long) URL
          <input name="long_url" type="url" />
        </label>
        <label>
          Title
          <input name="title" type="text" />
        </label>
        <button type="submit">URL Submitted</button>
      </Form>
    </>
  );
};

export default AddUrl;
