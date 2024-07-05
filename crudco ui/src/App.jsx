import { createBrowserRouter, RouterProvider } from "react-router-dom";
import ErrorPage from "./pages/ErrorPage";
import Home from "./routes/Home";
import Layout from "./pages/Layout";

import UrlList, { loader as UrlListloader } from "./components/UrlList";
import AddUrl, { action as AddUrlAction } from "./components/AddUrl";
import AddUser, { action as AddUserAction } from "./components/AddUser";
import Login, { action as LoginAction } from "./components/Login";

const router = createBrowserRouter([
  {
    element: <Layout />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/url-list",
        element: <UrlList />,
        loader: UrlListloader,
      },
      {
        path: "/add-url",
        element: <AddUrl />,
        action: AddUrlAction,
      },
      {
        path: "/add-user",
        element: <AddUser />,
        action: AddUserAction,
      },
      {
        path: "/Login",
        element: <Login />,
        action: LoginAction,
      },
    ],
  },
]);

const App = () => {
  return <RouterProvider router={router} />;
};

export default App;
