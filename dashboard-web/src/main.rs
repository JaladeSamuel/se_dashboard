#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;

use rocket_contrib::serve::StaticFiles;
use rocket_contrib::templates::Template;

use std::collections::HashMap;

#[get("/")]
fn index() -> Template {
    let context: HashMap<&str, &str> = [("name", "Jonathan")].iter().cloned().collect();
    Template::render("index", &context)
}

fn main() {
    rocket::ignite()
        .mount("/static", StaticFiles::from("static"))
        .mount("/", routes![index])
        .attach(Template::fairing())
        .launch();
}