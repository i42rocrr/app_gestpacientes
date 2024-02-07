package com.gestinterna.app.configuration;

import com.gestinterna.app.resultados.ResultadosPy;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.io.File;
import java.io.IOException;

@Configuration
public class ConfiguraPython {
    @Bean
    public ResultadosPy ConfResultadosPyImpl() {
        String venvExePath = new File("/graalenv/bin/graalpy")
                .getPath()
                .toString();

        Context contexto = Context
                .newBuilder("python")
                .allowAllAccess(true)
                .allowNativeAccess(true)
                .option("python.ForceImportSite", "true")
                .option("python.PythonPath", ".")
                .option("python.Executable", venvExePath)
                .option("python.NativeModules", "true")
                .build();
        try {
            Source source = Source
                    .newBuilder(
                    "python",
                            new File("/src/main/python/servicios/python_LaboratorioPacientes.py")
                            //new File("C:\\Users\\rafael.rojas\\Documents\\TFG\\GitHub\\app_gestinterna\\src\\main\\python\\servicios\\python_LaboratorioPacientes.py")
                    )
                    .build();

            contexto.eval(source);

            return contexto
                    .getBindings("python")
                    .getMember("ResultadosPyImpl")
                    .as(ResultadosPy.class);

        } catch (IOException ioException) {
            System.out.println("Algo pasó en el Bean de generación del context de python......................");
            System.out.println("-Causa del error: " + ioException.getCause());
            System.out.println("-Mensaje de error: " + ioException.getMessage());
            System.out.println("-Localizado en: " + ioException.getLocalizedMessage());
            return null;
        }

    }
}
