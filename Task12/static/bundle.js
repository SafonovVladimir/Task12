/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./assets/scripts/index.js":
/*!*********************************!*\
  !*** ./assets/scripts/index.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _likes__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./likes */ \"./assets/scripts/likes.js\");\n/* harmony import */ var _likes__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_likes__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _slideshow__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./slideshow */ \"./assets/scripts/slideshow.js\");\n/* harmony import */ var _slideshow__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_slideshow__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var _show_hide_text__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./show_hide_text */ \"./assets/scripts/show_hide_text.js\");\n/* harmony import */ var _show_hide_text__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_show_hide_text__WEBPACK_IMPORTED_MODULE_2__);\n\r\n\r\n\r\n\n\n//# sourceURL=webpack://task12/./assets/scripts/index.js?");

/***/ }),

/***/ "./assets/scripts/likes.js":
/*!*********************************!*\
  !*** ./assets/scripts/likes.js ***!
  \*********************************/
/***/ (() => {

eval("$(document).ready(function () {\r\n    $('.like_form').submit(function (e) {\r\n        e.preventDefault()\r\n\r\n        const post_id = $(this).attr('id')\r\n\r\n        const likeText = $(`.like-btn${post_id}`).text()\r\n        const trim = $.trim(likeText)\r\n\r\n        const url = $(this).attr('action')\r\n\r\n        let res;\r\n        const likes = $(`.like-count${post_id}`).text()\r\n        const trimCount = parseInt(likes)\r\n\r\n        $.ajax({\r\n            type: 'POST',\r\n            url: url,\r\n            data: {\r\n                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),\r\n                'post_id': post_id,\r\n            },\r\n            success: function (response) {\r\n                if (trim === 'Unlike') {\r\n                    $(`.like-btn${post_id}`).text('Like').removeClass('\"btn btn-danger like-btn{{ item.id }}').addClass('btn btn-success like-btn{{ item.id }}');\r\n                    res = trimCount - 1\r\n                } else {\r\n                    $(`.like-btn${post_id}`).text('Unlike').removeClass('\"btn btn-success like-btn{{ item.id }}').addClass('btn btn-danger like-btn{{ item.id }}');\r\n                    res = trimCount + 1\r\n                }\r\n                $(`.like-count${post_id}`).text(res)\r\n            },\r\n            error: function (response) {\r\n                console.log('error', response)\r\n            }\r\n        })\r\n    })\r\n});\n\n//# sourceURL=webpack://task12/./assets/scripts/likes.js?");

/***/ }),

/***/ "./assets/scripts/show_hide_text.js":
/*!******************************************!*\
  !*** ./assets/scripts/show_hide_text.js ***!
  \******************************************/
/***/ (() => {

eval("$(document).ready(function () {\r\n    // Configure/customize these variables.\r\n    var showChar = 70;  // How many characters are shown by default\r\n    var moretext = \"more\";\r\n    var lesstext = \"less\";\r\n\r\n\r\n    $('.more').each(function () {\r\n        var content = $(this).html();\r\n\r\n        if (content.length > showChar) {\r\n\r\n            var c = content.substr(0, showChar);\r\n            var h = content.substr(showChar, content.length - showChar);\r\n\r\n            var html = c + '&nbsp;<span class=\"moreellipses\">' + '...' + '&nbsp;</span><span ' +\r\n                'class=\"morecontent\"><span>' + h + '</span><a href=\"\" class=\"morelink\" style=\"text-decoration: none\">'\r\n                + moretext + '</a></span>';\r\n\r\n            $(this).html(html);\r\n        }\r\n\r\n    });\r\n\r\n    $(\".morelink\").click(function () {\r\n        if ($(this).hasClass(\"less\")) {\r\n            $(this).removeClass(\"less\");\r\n            $(this).html(moretext);\r\n        } else {\r\n            $(this).addClass(\"less\");\r\n            $(this).html(lesstext);\r\n        }\r\n        $(this).parent().prev().toggle();\r\n        $(this).prev().toggle();\r\n        return false;\r\n    });\r\n});\n\n//# sourceURL=webpack://task12/./assets/scripts/show_hide_text.js?");

/***/ }),

/***/ "./assets/scripts/slideshow.js":
/*!*************************************!*\
  !*** ./assets/scripts/slideshow.js ***!
  \*************************************/
/***/ (() => {

eval("let slideIndex = 1;\r\nshowSlides(slideIndex);\r\n\r\n// Next/previous controls\r\nfunction plusSlides(n) {\r\n    showSlides(slideIndex += n);\r\n}\r\n\r\n// Thumbnail image controls\r\nfunction currentSlide(n) {\r\n    showSlides(slideIndex = n);\r\n}\r\n\r\nfunction showSlides(n) {\r\n    let i;\r\n    let slides = document.getElementsByClassName(\"mySlides\");\r\n    let dots = document.getElementsByClassName(\"dot\");\r\n    if (n > slides.length) {\r\n        slideIndex = 1\r\n    }\r\n    if (n < 1) {\r\n        slideIndex = slides.length\r\n    }\r\n    for (i = 0; i < slides.length; i++) {\r\n        slides[i].style.display = \"none\";\r\n    }\r\n    for (i = 0; i < dots.length; i++) {\r\n        dots[i].className = dots[i].className.replace(\" active\", \"\");\r\n    }\r\n    slides[slideIndex - 1].style.display = \"block\";\r\n    dots[slideIndex - 1].className += \" active\";\r\n}\n\n//# sourceURL=webpack://task12/./assets/scripts/slideshow.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./assets/scripts/index.js");
/******/ 	
/******/ })()
;