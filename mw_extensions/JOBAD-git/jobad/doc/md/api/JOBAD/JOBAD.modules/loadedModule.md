# JOBAD.modules.loadedModule

* **Function** `JOBAD.modules.loadedModule(name, args, JOBADInstance, callback)` Loads a module, assuming the dependencies are already available. 
	* **String** `name` Module to load.
	* **Array[Mixed]** Arguments to pass to this module instance. 
	* **Instance[ [JOBAD](../JOBADInstance/index.md) ]** `JOBADInstance` The instance of JOBAD the module is initiated on. 
	* **Function** `callback(state)` Callback. Will be called when the module has finsihed loading or fails to do so. 
	* **returns** a new `JOBAD.modules.loadedModule` instance. 

## Instance Functions

* **Function** `.info()` Returns the info object of this module. 
* **Function** `.getJOBAD()` Gets the `JOBADInstance` this module is bound to. 

* **Function** `.isActive()` Checks if this module is active. 
* **Function** `.activate()` Activates this module. 
* **Function** `.deactivate()` Deactivates this module

## UserConfiguration

* **Function** `.UserConfig.set(prop, value)` Updates user configuration. 
	* **String** `prop` Property to set. 
	* **Mixed** `value` Value to set. 

* **Function** `.UserConfig.canSet(prop, value)` Checks if a user configuration can be set with the specefied value. 
	* **String** `prop` Property to set. 
	* **Mixed** `value` Value to set. 
	* **returns** boolean. 

* **Function** `.UserConfig.get(prop)` Reads user configuration. 
	* **String** `prop` Property to get. 
	* **returns** value. 

* **Function** `.UserConfig.setMessage(msg)` Sets the current message (displayed in config UI). 
	* **String** `msg` Message to set. 
* **Function** `.UserConfig.getMessage()` Gets the current message (displayed in config UI). 


* **Function** `.UserConfig.reset()` Resets the user configuration. 
* **Function** `.UserConfig.getTypes()` Gets the user configuration types. 



## Event functions

These functions represent event handlers. If an event is globally disabled (via  [`JOBAD.config.disabledEvents`](../JOBAD.config.md)) it will not show up in the JOBAD.modules.loadedModule Instance. 

* **Function** `.onActivate(JOBADInstance)` Called on module activation. 
	* **Instance[ [JOBAD](../JOBADInstance/index.md) ]** `JOBADInstance` A reference to `.getJOBAD()`. 
* **Function** `.onDeactivate(JOBADInstance)` Called on module deactivation. 
	* **Instance[ [JOBAD](../JOBADInstance/index.md) ]** `JOBADInstance` A reference to `.getJOBAD()`. 
* **Function** `.leftClick(target, JOBADInstance)` Simulate a left click event to pass to the Module. 
	* **jQuery** `target` The element to simulate clicking on. 
	* **Instance[ [JOBAD](../JOBADInstance/index.md) ]** `JOBADInstance` A reference to `.getJOBAD()`. 
	* **returns** `true` if it performed some action, `false` otherwise. 
* **Function** `.contextMenuEntries(target, JOBADInstance)` Simulate a context menu request to the module. 
	* **jQuery** `target` The element to simulate a context menu request on. 
	* **returns** a list of `[name, callback]` and `[name, submenu]` pairs or false if nothing should be done. 
* **Function** `.hoverText(target, JOBADInstance)` Simulate hovering over an element. 
	* **jQuery** `target` The element to simulate hovering on. 
	* **Instance[ [JOBAD](../JOBADInstance/index.md) ]** `JOBADInstance` A reference to `.getJOBAD()`. 
	* **returns** a text to use as hover text, a jQuery-ish object[^1] or a boolean. 
* **Function** `.onSideBarUpdate(JOBADInstance)` Simulate a sidebar update. 
	* **Instance[ [JOBAD](../JOBADInstance/index.md) ]** `JOBADInstance` A reference to `.getJOBAD()`. 
	* **returns** a text to use as hover text, a jQuery-ish object[^1] or a boolean. 
	


## .localStore

* **Object** `.localStore` Namespace to store variables bound to this instance of a module. 
* **Function** `.localStore.get(key)` Gets a local variable. 
	* **String** `key` Name of variable to get. 
	* **returns** the variable or undefined. 
* **Function** `.localStore.set(key, value)` Sets a local variable. 
	* **String** `key` Name of variable to get. 
	* **Mixed** `value` Value to set the variable to. 
* **Function** `.localStore.delete(key)` Deletes a local variable. 
	* **String** `key` Key to delete. 
* **Function** `.localStore.keys()` Gets all available keys. 
	
## .globalStore
* **Object** `.globalStore` Namespace to store variables shared among instances of this variable. 
* **Function** `.globalStore.get(key)` Gets a global variable. 
	* **String** `key` Name of variable to get. 
	* **returns** the variable or undefined. 
* **Function** `.globalStore.set(key, value)` Sets a global variable. 
	* **String** `key` Name of variable to get. 
	* **Mixed** `value` Value to set the variable to. 
* **Function** `.globalStore.delete(key)` Deletes a global variable. 
	* **String** `key` Key to delete. 
* **Function** `.globalStore.keys()` Gets all available keys. 

## Further members
A `JOBAD.modules.loadedModule` instance also contains all non-standard properties of the original Module object. Note
that any JSON-style objects are referenced (and thus shared among all instances of this module) and everything else 
is copied. 


## Footnotes
[^1]: A jQuery-ish object is any object that can be passed to the main jQuery function, for example a document node or a jQuery selector. 
