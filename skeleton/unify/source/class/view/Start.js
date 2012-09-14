/* ************************************************************************

  ${NAMESPACE}

 ************************************************************************ */

/**
 * Start View
 */
core.Class("$${name}.view.Start", {
  include : [unify.view.StaticView],

  construct : function() {
    unify.view.StaticView.call(this);
  },

  members : 
  {
    // overridden
    getTitle : function(type, param) {
      return "Start";
    },

    
    // overridden
    _createView : function() {
      var content = new unify.ui.basic.Label("Hello World");
      this.add(content);
    }
  }
});

unify.core.Singleton.annotate($${name}.view.Start);
