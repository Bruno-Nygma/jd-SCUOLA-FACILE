import "./style.css";
import { createRoot } from "just-dom";
import { jd } from "./jd.config.js";
import { defineRoutes } from "@just-dom/router";
import { DashboardPage } from "./pages/dashboard-page.js";
import { DashboardLayout } from "./layouts/dashboard-layout.js";
import { StudentsListPage } from "./pages/students-list-page.js";
import { StudentPage } from "./pages/student-page.js";

const routes = defineRoutes([
  {
    layout: DashboardLayout, 
    children: [
      { path: '/dashboard', element: DashboardPage},
      { path: '/studenti', element: StudentsListPage},
      { path: '/studenti/:id', element: StudentPage}
      //@TODO: pagina not-found 
    ]
  }
])

createRoot(
  "app",
  jd.router(routes)
);
