import { useLoaderData } from "react-router-dom";
// import { getUrls } from "../api";

export async function loader() {
  const response = await fetch("http://localhost:8000/url-list");
  const data = await response.json();

  return {data};}

const UrlList = () => {
  const { data } = useLoaderData();

  return (
    <div>
      <h2 className= "URLList">URL List</h2>
     
      <ul>
        {data.map((url) => (
          <li key={url.id}>
            {url.title}:{url.short_url} ({url.long_url})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UrlList;
