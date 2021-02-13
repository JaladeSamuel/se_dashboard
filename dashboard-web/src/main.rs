#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;

use rocket_contrib::serve::StaticFiles;
use rocket_contrib::templates::Template;

use std::collections::HashMap;

#[get("/toulouse")]
fn toulouse() -> Template {
    let context: HashMap<&str, &str> = [("", "")].iter().cloned().collect();
    Template::render("toulouse", &context)
}

#[get("/new_york")]
fn new_york() -> Template {
    let context: HashMap<&str, &str> = [("", "")].iter().cloned().collect();
    Template::render("new_york", &context)
}

#[get("/london")]
fn london() -> Template {
    let context: HashMap<&str, &str> = [("", "")].iter().cloned().collect();
    Template::render("london", &context)
}

#[get("/moscou")]
fn moscou() -> Template {
    let context: HashMap<&str, &str> = [("", "")].iter().cloned().collect();
    Template::render("moscou", &context)
}

#[get("/rio")]
fn rio() -> Template {
    let context: HashMap<&str, &str> = [("", "")].iter().cloned().collect();
    Template::render("rio", &context)
}

#[get("/map")]
fn map() -> Template {
    let context: HashMap<&str, &str> = [("", "")].iter().cloned().collect();
    Template::render("map", &context)
}

#[get("/")]
fn index() -> Template {
    let context: HashMap<&str, &str> = [("", "")].iter().cloned().collect();
    Template::render("index", &context)
}

fn main() {
    rocket::ignite()
        .mount("/", StaticFiles::from("static"))
        .mount("/", routes![index, toulouse, london, new_york, moscou, rio, map])
        .attach(Template::fairing())
        .launch();
}