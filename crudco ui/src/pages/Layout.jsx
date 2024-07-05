import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <nav className="navBar">
        <Link to="/">Home</Link>

        <Link to="/Login"> Login</Link>

        <Link to="/url-list"> URL List</Link>

        <Link to="/add-url"> Add URL </Link>

        <Link to="/add-user"> Add User</Link>
      </nav>
      <Outlet />
    </>
  );
};

export default Layout;
