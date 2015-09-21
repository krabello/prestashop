<?php

class CatalogSolutionsHerhis extends module
{
     
    public function __construct()
    {
        // Set the technical name. W/O this the module will
        // not be able to be installed
        $this->name = 'herhis';
     
        // Set the Public name. This line is used to display
        // the module name for the merchant in the modules
        // list of the back office
        $this->displayName = 'Her his';
         
        // Set the module category (optional) makes the module search easier
        // administration
        // advertising_marketing
        // analytics_stats
        // billing_invoicing
        // Checkout
        // content_management
        // export
        // emailing
        // front_office_features
        // i18n
        // localization
        // merchandizing
        // migration_tools
        // payments_gateways
        // payment_security
        // pricing_promotion
        // quick_bulk_update
        // search_filter
        // seo
        // shipping_logistics
        // slideshows
        // smart_shopping
        // market_place
        // social_networks
        // others (default)
        // mobile
        $this->tab = 'others';
        
        // Set the module version
        // display the module version in the module's 
        // list of the back office but also to check 
        // if updates are available
        $this->version = '1.0.0';
        
        // Set the author name: This line is used to 
        // display the author name for the merchant in 
        // the module's list of the back office. It can also 
        // be used to search for modules:
        $this->author = 'Catalog Solutions';
        
        // Set the module description
        $this->description = '';
        
        // Call the parent contstructor. initializations
        // are made in this function.
        parent::__construct();
     
    }
}
