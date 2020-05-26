/*
A KBase module: jsfillman_ghaction
This sample module contains one small method that filters contigs.
*/

module jsfillman_ghaction {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_jsfillman_ghaction(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
