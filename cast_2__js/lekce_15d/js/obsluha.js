'use strict';

const microsoft = new Firma("Microsoft", "Redmond, WA");
const google = new Firma("Google", "Mountain View, CA");
const apple = new Firma("Apple", "Cupertino, CA");

microsoft.vypisInfoOFirme();
google.vypisInfoOFirme();
apple.vypisInfoOFirme();

microsoft.pridejZamestnance();
microsoft.vypisZamestnance();