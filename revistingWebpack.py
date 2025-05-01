'''
we can write npm scripts in package.json by adding
a scripts for ex:


{
  // ... other package.json stuff
  "scripts": {
    "build": "webpack",
    "dev": "webpack serve",
    "deploy": "git subtree push --prefix dist origin gh-pages"
  },
  // ... other package.json stuff
}


then we can run 

npm run build == npm webpack

as well 

npm run dev == git subtree push --prefix dist origin gh-pages

 
where do npm scripts live : 

in package.json with a "scripts" property

how do you definte and run npm scripts:

"command : "clt command'

the two webpack modes are build and dev
webpack merge allows us to split multiple webpack config files

template repository can convert an existing reporisorty to a template

'''


